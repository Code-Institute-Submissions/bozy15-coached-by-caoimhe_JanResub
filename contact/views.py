from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .forms import ContactForm


def contact_form(request):
    """A view to submit the form and send it to site owner"""

    # If the form is submitted
    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        form = ContactForm(request.POST)
        # Check whether it's valid
        if form.is_valid():
            # get user email from form
            user_email = form.cleaned_data["email"]
            # Subject of the email
            subject = form.cleaned_data["subject"]
            # Put the body of the email in a dictionary
            body = {
                "My name is": form.cleaned_data["full_name"],
                "My email is": form.cleaned_data["email"],
                "My message is": form.cleaned_data["message"],
            }
            # Join the dictionary into a string
            message = "\n".join(["{}: {}".format(k, v) for k, v in body.items()])
            # Send the email
            try:
                send_mail(subject, message, user_email, [settings.DEFAULT_FROM_EMAIL])
            # If the email fails to send
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            # If everything is fine, refresh the page
            template = "contact/contact.html"
            return render(request, template)
    # If the form is not submitted
    form = ContactForm()
    # Get google maps api key from settings.py
    google_maps_api_key = settings.GOOGLE_MAPS_API_KEY
    template = "contact/contact.html"
    context = {
        "form": form,
        "google_maps_api_key": google_maps_api_key,
    }
    return render(request, template, context)
