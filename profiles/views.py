from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

@login_required
def profile(request):
    """""
    Profile page for the user.
    """
    #Get the user profile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Save data if the form is submitted
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
        else:
            messages.error(request, 'Update failed. Please correct the error.')
    else:
        form = UserProfileForm(instance=profile)

    # Get all orders for the user
    orders = profile.orders.all()
    
    # The template that will be rendered
    template = "profiles/profile.html"
    
    context = {
        'form': form,
        'orders': orders,
        # Prevents cart being displayed on profile page
        'on_profile_page': True
    }

    # Render the template
    return render(request, template, context)

def order_history(request, order_number):
    """
    View for the order history page.
    """
    # Get the order
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f"This is a past confirmation for order number {order_number}. "
        "A confirmation email was sent on the order date."
    ))
    # The template that will be rendered
    template = "checkout/checkout_success.html"
    # Context to pass to template
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)