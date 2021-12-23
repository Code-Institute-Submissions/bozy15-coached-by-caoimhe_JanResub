from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    # Get cart from session
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "Your cart is empty")
        return redirect(reverse("workouts"))

    # Instance of the OrderForm
    order_form = OrderForm()
    # Create the template
    template = "checkout/checkout.html"
    # Context
    context = {
        "order_form": order_form,
        "cart": cart,
        "stripe_public_key": "pk_test_51K9wLkABg1AD6xDhx9PjXsz275wDhW8nnpIMpblyse70oNgHKhLwEhGwMBnakxzEKl58gJxPROlrd55PxMAM0VrV00OjPUyJEn",
        "client_secret": "test client secret",
    }
    # Render the template
    return render(request, template, context)
