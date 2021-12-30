from django import forms

from .models import Subscribe

class SubscribeForm(forms.ModelForm):
    """A form to subscribe the user to the newsletter"""
    class Meta:
        model = Subscribe
        fields = ("email",)