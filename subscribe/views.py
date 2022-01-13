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
        # Create an instance of the form
        form = SubscribeForm(request.POST)
        # Get all email values from database
        email_list = Subscribe.objects.values_list('email', flat=True)
        # Check if the email is already in the database
        if request.POST['email'] in email_list:
            messages.error(request, "You are already subscribed to our newsletter")
            return render(request, "home/index.html", {"form": form})
        # check if the form is valid
        elif form.is_valid():
            # Save the form data to the database
            user_email = form.cleaned_data.get("email")
            print(user_email)
            form.save()
            form = SubscribeForm()
            # Send email to the user
            try:
                send_mail(
                    "Coached By Caoimhe email subscription",
                    "Thank you for subscribing to our newsletter",
                    settings.EMAIL_HOST_USER,
                    [user_email],
                    fail_silently=False,  # If the email fails to send, it will raise an error
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            # display toast
            messages.success(request, "Thank you for subscribing!")
        else:
            messages.error(request, "Please enter a valid email address")
    else:
        form = SubscribeForm()

    return render(request, "home/index.html", {"form": form})
