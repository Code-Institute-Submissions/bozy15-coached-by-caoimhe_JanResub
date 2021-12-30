from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        # The model to use for the form
        model = UserProfile
        # exclude the user field, can't be edited
        exclude = ("user",)
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """Add placeholder and classes, remove labels and set autofocus on first field"""
        # Call the parent's __init__ method before we do anything
        super().__init__(*args, **kwargs)
        # Change the labels
        placeholders = {
            "default_full_name": "Full Name",
            "default_email": "Email Address",
            "default_phone_number": "Phone Number",
            "default_postcode": "Postcode",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County, State or Region",
        }
        # set autofocus on first field
        self.fields["default_email"].widget.attrs["autofocus"] = True
        # Loop through the fields and set the placeholder
        for fields in self.fields:
            if fields != "default_country":
                if self.fields[fields].required:
                    # Add an asterisk to the placeholder if the field is required
                    placeholder = f"{placeholders[fields]} *"
                else:
                    placeholder = placeholders[fields]
                # Set the placeholder to the value of the dictonary above
                self.fields[fields].widget.attrs["placeholder"] = placeholder
            # Add CSS class to the field
            self.fields[fields].widget.attrs[
                "class"
            ] = "rounded-2 profile-form-input form-control"
            # Remove the labels
            self.fields[fields].label = False
