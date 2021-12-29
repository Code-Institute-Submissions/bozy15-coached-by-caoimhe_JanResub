from django.db import models
from django.contrib.auth.models import User

# Category model
class Category(models.Model):
    """
    Model for the categories of the workouts.
    Name is used programmatically, friendly_name is used for the user.
    """

    # Changes the name from categorys to categories in admin
    class Meta:
        verbose_name_plural = "Categories"

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

    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=254)
    description = models.TextField()
    equipment_required = models.TextField(default="")
    weekly_checkin = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    length_of_workout = models.TextField(null=True, blank=True)
    plan_duration = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # __str__ is used to return the name of the workout
    def __str__(self):
        return self.name

    # get_friendly_name is used to return the friendly_name of the workout
    def get_friendly_name(self):
        return self.friendly_name


class WorkoutReview(models.Model):
    """
    A model for the reviews of the workouts.
    """

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Workout Reviews"

    # tuple of the fields that can be picked
    stars = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    )

    # The workout the review is for
    workout = models.ForeignKey(
        Workout, null=True, blank=True, on_delete=models.SET_NULL
    )
    # The user who wrote the review
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE
    )
    # the review title, can be left blank
    review_title = models.CharField(max_length=254, null=True, blank=True)
    # Comment can be left blank
    comment = models.TextField(blank=True, null=True)
    # Must leave a rating
    rating = models.IntegerField(choices=stars, default=5)
    # date the review was written
    date = models.DateTimeField(auto_now_add=True)

    # __str__ is used to return the name of the workout
    def __str__(self):
        return self.review_title
