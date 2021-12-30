from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

from .models import Subscribe
from .forms import SubscribeForm


def subscribe_form(request):
    """
    A view to save the users email to the database and send email to them
    """
    form = SubscribeForm()

    # If the form is submitted
    if request.method == "POST":
        # create an instance of the form
        form = SubscribeForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            user_email = form.cleaned_data.get("email")
            print(user_email)
            form.save()
            form = SubscribeForm()
            # display toast
            messages.success(request, "Thank you for subscribing!")
        else:
            messages.error(request, "Please enter a valid email address")
    else:
        form = SubscribeForm()

    return render(request, "home/index.html", {"form": form})
