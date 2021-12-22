from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Order, OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_order_total(sender, instance, created, **kwargs):
    """Update the total of the order when a line item is added or removed"""
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_order_total(sender, instance, **kwargs):
    """Update the total of the order when a line item is added or removed"""
    instance.order.update_total()