import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.db.models.fields import CharField
from django_countries.fields import CountryField

from workouts.models import Workout


class Order(models.Model):
    """Creates order model containing the data for the order"""

    order_number = models.CharField(
        max_length=32, null=False, editable=False
    )  # automatically generated, unable to edit
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country*", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    # Prevent errors if user buys same item twice on different occasions
    original_cart = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default="")

    def _generate_order_number(self):
        """Generate random, unique number using UUID"""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """Update total each time a line item is added or removed"""
        self.total = (
            self.lineitems.aggregate(Sum("lineitem_total"))["lineitem_total__sum"] or 0
        )
        self.save()

    def save(self, *args, **kwargs):
        """Override the original save method to the order number"""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """Creates order line item model containing the data for each item in the order"""

    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    workout = models.ForeignKey(
        Workout, null=False, blank=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """Override the original save method to the line item total"""
        self.lineitem_total = self.workout.price * self.quantity
        super().save(*args, **kwargs)

    # returns the workout name and order number
    def __str__(self):
        return f"{self.workout.name} on order {self.order.order_number}"
