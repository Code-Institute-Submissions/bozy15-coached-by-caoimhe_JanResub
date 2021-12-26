from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineAdminInline,)

    # Prevent admin from editing these order fields
    readonly_fields = ("order_number", "date", "total", "stripe_pid", "original_cart")

    # Display these fields when viewing an order
    fields = (
        "order_number",
        "user",
        "date",
        "full_name",
        "email",
        "phone_number",
        "country",
        "postcode",
        "town_or_city",
        "street_address1",
        "street_address2",
        "county",
        "total",
        "stripe_pid",
        "original_cart"
    )

    # restrict which fields that show up in the list
    list_display = ("order_number", "date", "full_name", "total")

    # Order by date
    ordering = ("-date",)


# Register the Order model with the admin site
admin.site.register(Order, OrderAdmin)
