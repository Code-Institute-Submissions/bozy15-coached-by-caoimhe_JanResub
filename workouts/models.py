from django.db import models
from django.contrib.auth.models import User

# Category model
class Category(models.Model):
    """
    Model for the categories of the workouts.
    Name is used programmatically, friendly_name is used for the user.
    """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # __str__ is used to return the name of the category
    def __str__(self):
        return self.name

    # get_friendly_name is used to return the friendly_name of the category
    def get_friendly_name(self):
        return self.friendly_name

class Workout(models.Model):
    """
    Model for the workouts containing data about each plan.
    Name is used programmatically, friendly_name is used for the user.
    """

    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    length_of_workout = models.TextField(null=True, blank=True)
    weeks_of_plan = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # __str__ is used to return the name of the workout
    def __str__(self):
        return self.name

    # get_friendly_name is used to return the friendly_name of the workout
    def get_friendly_name(self):
        return self.friendly_name