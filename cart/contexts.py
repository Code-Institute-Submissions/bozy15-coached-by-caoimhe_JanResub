from django.shortcuts import get_object_or_404
from workouts.models import Workout


def cart_contents(request):
    """Function to return a dictionary to all templates"""

    # list to hold the cart contents
    cart_items = []
    # Total cost in cart
    total = 0
    # Total quantity in cart, should not be greater than 1
    plan_count = 0
    # Access the cart session
    cart = request.session.get("cart", {})

    # Loop through the cart and add the items to the cart_plan list
    for item_id, quantity in cart.items():
        workout = get_object_or_404(Workout, pk=item_id)
        total += workout.price * quantity
        plan_count += quantity
        # Add a dictionary to the cart_plan list, 
        # give access to all the workout details
        cart_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "workout": workout,
            }
        )

    context = {
        "cart_items": cart_items,
        "total": total,
        "plan_count": plan_count,
    }

    return context
