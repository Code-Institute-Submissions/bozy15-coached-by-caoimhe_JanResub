from django import forms

class ContactForm(forms.Form):
    """ Contact form for users to get in touch with the site owner. """

    full_name = forms.CharField(max_length=60, required=True)
    email = forms.EmailField(max_length=254, required=True)
    subject = forms.CharField(max_length=60, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=1500)
