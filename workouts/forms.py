from django import forms
from .models import Workout, Category


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        # Include all the fields from the model
        fields = "__all__"
    
    # Override the default __init__ method to add a custom form field
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get all the categories from the Category model
        categories = Category.objects.all()
        # Create a list of tuples
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # Add the friendly_names field to the form
        self.fields['category'].choices = friendly_names
        # Add a custom CSS class to the category field
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border-2'
