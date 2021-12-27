from django.http.response import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from .forms import OrderForm
from .models import Order, OrderLineItem

from workouts.models import Workout
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """Captures data from stripe and saves it in PaymentIntent"""

    try:
        # Get the payment intent id
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Modify the payment intent
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "cart": json.dumps(request.session.get("cart", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be \
            processed right now. Please try again later.",
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    # stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Create order in database and redirect to success page
    if request.method == "POST":
        cart = request.session.get("cart", {})

        # Put data from the checkout form into dictionary
        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "county": request.POST["county"],
        }

        # Create am instance of the order form
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # Save the order form to the database
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            # loop through the cart items and create order line items
            for item_id, item_data in cart.items():
                try:
                    workout = Workout.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            workout=workout,
                            quantity=item_data,
                        )
                        # Save the order line item to the database
                        order_line_item.save()
                # If the workout does not exist
                # Display error message, delete order and redirect to cart
                except Workout.DoesNotExist:
                    messages.error(
                        request,
                        "This item does not seem to exist \
                        in our database. Please try again. \
                        If the problem persists please contact us.",
                    )
                    order.delete()
                    return redirect(reverse("view_cart"))
            # Save the info fron the checkout page if user checked the box
            request.session["save_info"] = order_form.cleaned_data
            return redirect(reverse("checkout_success", args=[order.order_number]))
        else:
            messages.error(
                request,
                "There was an error with your form. \
                                    Please double check your information.",
            )
    else:
        # Get cart from session
        cart = request.session.get("cart", {})
        if not cart:
            messages.error(request, "Your cart is empty")
            return redirect(reverse("workouts"))

        # Get the cart contents
        current_cart = cart_contents(request)
        # Get the total cost
        total = current_cart["total"]
        # Stripe total
        stripe_total = round(total * 100)
        # Stripe API
        stripe.api_key = stripe_secret_key
        # Create the stripe session
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Populate the order form with the data from user profile
        if request.user.is_authenticated:
            try:
                # Get the user profile
                profile = UserProfile.objects.get(user=request.user)
                # Populate the order form with the data from user profile
                order_form = OrderForm(initial={
                    "full_name": profile.user.get_full_name(),
                    "email": profile.user.email,
                    "phone_number": profile.default_phone_number,
                    "street_address1": profile.default_street_address1,
                    "street_address2": profile.default_street_address2,
                    "town_or_city": profile.default_town_or_city,
                    "postcode": profile.default_postcode,
                    "county": profile.default_county,
                    "country": profile.default_country, 
                })
            # If the user does not have a profile
            except UserProfile.DoesNotExist:
                # Create an empty order form
                order_form = OrderForm()
        else:
            # Create the order form
            order_form = OrderForm()
        

    # if public key is not set
    if not stripe_public_key:
        messages.warning(
            request,
            "Stripe public key is missing.\
            You need to set it in your environment variables",
        )

    # Create the template
    template = "checkout/checkout.html"
    # Context
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    # Render the template
    return render(request, template, context)


def checkout_success(request, order_number):
    """This view will handle the successful checkouts"""

    # Check if user has checked the box to save info
    save_info = request.session.get("save_info")
    # Get order
    order = get_object_or_404(Order, order_number=order_number)

    # Get user if logged in
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Save the user's info to profile
        order.user_profile = profile
        order.save()

        # If user has checked the box to save info
        if save_info:
            profile_data = {
                "default_email": save_info["email"],
                "default_phone_number": save_info["phone_number"],
                "default_country": save_info["country"],
                "default_postcode": save_info["postcode"],
                "default_town_or_city": save_info["town_or_city"],
                "default_street_address1": save_info["street_address1"],
                "default_street_address2": save_info["street_address2"],
                "default_county": save_info["county"],
            }
            # Update the user profile
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(
        request,
        f"Order successfully processed! \
                                Your order number is {order_number}. \
                                    A confirmation email will be sent to {order.email}.",
    )

    # Clear the cart
    if "cart" in request.session:
        del request.session["cart"]

    # Set the template and context
    # Then render template
    template = "checkout/checkout_success.html"
    context = {"order": order}
    return render(request, template, context)
