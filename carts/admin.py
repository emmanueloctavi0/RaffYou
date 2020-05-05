
# Django
from django.contrib import admin

# Models
from carts.models import Cart
from products.models import Product

class ProductInline(admin.TabularInline):
    model = Product.cart_set.through
    extra = 1


class CartAdmin(admin.ModelAdmin):
    inlines = [ProductInline,]


admin.site.register(Cart, CartAdmin)
