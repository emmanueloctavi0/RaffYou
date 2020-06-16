
# Django
from django.contrib import admin

# Models
from carts.models import Cart, PromotionalCode
from products.models import ProductPrice

class ProductInline(admin.TabularInline):
    model = ProductPrice.cart_set.through
    extra = 1


class PromotionalCodeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'code',
        'cart_discount',
        'discount_mount',
        'expiry_datetime',
        'is_active',
    )

    list_display_links = [
        'id',
        'name',
        'code',
    ]


class CartAdmin(admin.ModelAdmin):
    inlines = [ProductInline,]


admin.site.register(Cart, CartAdmin)
admin.site.register(PromotionalCode, PromotionalCodeAdmin)
