from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile


@login_required
def profile(request):
    """""
    Profile page for the user.
    """
    #Get the user profile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Save data if the form is submitted
    #
    # Get all orders for the user
    orders = profile.orders.all()

    # The template that will be rendered
    template = "profiles/profile.html"
    
    context = {
       # 'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    # Render the template
    return render(request, template, context)
