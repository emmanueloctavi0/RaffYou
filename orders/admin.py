
# Django
from django.contrib import admin

# Models
from orders.models import Order
from products.models import ProductPrice

# Utilities
from django.utils.html import format_html


class ProductsInline(admin.TabularInline):
    model = ProductPrice.order_set.through
    extra = 0
    can_delete = False
    readonly_fields = [
        'product',
        'amount',
        'provider',
        'address',
    ]

    def provider(self, obj):
        """Get name provider"""
        return obj.product.product.provider.name

    def address(self, obj):
        return obj.product.product.provider.first_address

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'telephone',
        'status',
        'address_reference',
        'name',
    ]

    list_editable = ['status',]

    readonly_fields = ('name', '_address')

    exclude = ['user', 'address']

    inlines = [
        ProductsInline,
    ]

    def telephone(self, order):
        return format_html(
            '<a target="_blank" href="https://wa.me/052{}?text=">{}</a>',
            order.address.telephone,
            order.address.telephone,
        )

    def name(self, order):
        return order.address.name

    def address_reference(self, order):
        return format_html(
            '<a target="_blank" href="https://waze.com/ul?q={} {} {} {}">{}</a>',
            order.address.street_name,
            order.address.street_number,
            order.address.colony,
            order.address.city,
            order.address.references,
        )

    def _address(self, order):
        return format_html(
            '<p>{}, {}, {}, {}, {}</p>',
            order.address.street_name,
            order.address.street_number,
            order.address.colony,
            order.address.city,
            order.address.references,
        )

admin.site.register(Order, OrderAdmin)
