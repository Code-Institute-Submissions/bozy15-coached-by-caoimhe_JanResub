from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    # stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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

    # Instance of the OrderForm
    order_form = OrderForm()
    
    # if public key is not set
    if not stripe_public_key:
        messages.warning(request, "Stripe public key is missing.\
            You need to set it in your environment variables")

    # Create the template
    template = "checkout/checkout.html"
    # Context
    context = {
        "order_form": order_form,
        "cart": cart,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }
    
    # Render the template
    return render(request, template, context)
