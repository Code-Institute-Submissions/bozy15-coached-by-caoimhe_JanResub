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
    }
    # Render the template
    return render(request, template, context)
