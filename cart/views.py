from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from django.contrib import messages

from workouts.models import Workout


def view_cart(request):
    """A view that renders the cart contents page"""

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """Add a specified product to the cart"""

    # Get workout from database
    workout = get_object_or_404(Workout, pk=item_id)
    # Get redirect url so user can be redirected to the page they were on
    redirect_url = request.POST.get("redirect_url")
    # Store session key in a variable to allow user to move through site without losing session
    cart = request.session.get("cart", {})
    # If item is already in cart, do not increase quantity by 1
    if item_id in list(cart.keys()):
        cart[item_id] = 1
        # item_id already in cart, show message
        messages.info(request, f"{workout.name} has already been added to your cart!")
    # If item is not in cart, add it to cart
    else:
        cart[item_id] = 1
        messages.success(request, f"{workout.name} has been added to your cart!")

    # Update session cart
    request.session["cart"] = cart
    # Redirect user to the page they were on
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove a specified product from the cart"""

    # Get workout from database
    workout = get_object_or_404(Workout, pk=item_id)

    try:
        # Store session key in a variable to allow user to move through site without losing session
        cart = request.session.get("cart", {})

        # If item is in cart, remove it from cart
        if item_id in list(cart.keys()):
            cart.pop(item_id)
            messages.success(
                request, f"{workout.name} has been removed from your cart!"
            )

        # Update session cart
        request.session["cart"] = cart
        # Redirect user to the page they were on
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(f"Error: {e}", status=500)
