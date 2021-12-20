from django.shortcuts import redirect, render


def view_cart(request):
    """A view that renders the cart contents page"""

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """Add a specified product to the cart"""

    # Get redirect url so user can be redirected to the page they were on
    redirect_url = request.POST.get("redirect_url")
    # Store session key in a variable to allow user to move through site without losing session
    cart = request.session.get("cart", {})

    # If item is already in cart, do not increase quantity by 1
    if item_id in list(cart.keys()):
        cart[item_id] = 1
    # If item is not in cart, add it to cart
    else:
        cart[item_id] = 1

    # Update session cart
    request.session["cart"] = cart
    # Redirect user to the page they were on
    return redirect(redirect_url)