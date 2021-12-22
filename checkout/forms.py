from django import forms

from .models import Order, OrderLineItem


class OrderForm(forms.ModelForm):
    class Meta:
        # The model to use for the form
        model = Order
        # The fields to render in the form
        fields = (
            "full_name",
            "email",
            "phone_number",
            "country",
            "postcode",
            "town_or_city",
            "street_address1",
            "street_address2",
            "county",
        )

    def __init__(self, *args, **kwargs):
        """Add placeholder and classes, remove labels and set autofocus on first field"""
        # Call the parent's __init__ method before we do anything
        super().__init__(*args, **kwargs)
        # Change the labels
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "country": "Country",
            "postcode": "Postcode",
            "town_or_city": "Town or City",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "county": "County",
        }
        # set autofocus on first field
        self.fields["full_name"].widget.attrs["autofocus"] = True
        # Loop through the fields and set the placeholder
        for fields in self.fields:
            if self.fields[fields].required:
                # Add an asterisk to the placeholder if the field is required
                placeholder = f"{placeholders[fields]} *"
            else:
                placeholder = placeholders[fields]
            # Set the placeholder to the value of the dictonary above
            self.fields[fields].widget.attrs["placeholder"] = placeholder
            # Add CSS class to the field
            self.fields[fields].widget.attrs["class"] = "stripe-style-input"
            # Remove the labels
            self.fields[fields].label = False
