# From boutique-ado: checkout\webhook_handler.py

from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from workouts.models import Workout
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            "checkout/confirmation_emails/confirmation_email_subject.txt",
            {"order": order},
        )
        body = render_to_string(
            "checkout/confirmation_emails/confirmation_email_body.txt",
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
        )
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        # Store intent details
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        # Store payment details

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details to prevent errors
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_full_name = shipping_details.name
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        # Set order to false if it doesn't exist
        order_exists = False
        # Precaution to prevent duplicate orders
        # if sever is slow and webhook hasn't found the order
        attempt = 1
        while attempt <= 5:
            # Try finding the order
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    total=total,
                    # Details needed so same user can purchase same item
                    # on different occasion
                    original_cart=cart,
                    stripe_pid=pid,
                )
                print("this is original cart", order.original_cart)
                # if order exists set booleen and break loop
                order_exists = True
                break
            # if order doesn't exist, try again
            except Order.DoesNotExist:
                # increment attempt and wait 1 second before trying again
                attempt += 1
                time.sleep(1)
        # if order exists, update the order
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: \
                          Verified order already in database',
                status=200,
            )
        else:
            # if the order doesn't exist create a new order
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    # Details needed so same user can purchase same item
                    # on different occasion
                    original_cart=cart,
                    stripe_pid=pid,
                )
                # iterate through cart from payment intent and find order details
                for item_id, item_data in json.loads(cart).items():
                    workout = Workout.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            workout=workout,
                            quantity=item_data,
                        )
                        order_line_item.save()
            # if anything goes wrong, delete the order and return an error
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500,
                )
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: \
                      Created order in webhook',
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)
