
# Django
from django.contrib import admin

# Models
from products.models import (
    Product, ProductTag, ProductPrice,
    Provider
)


class PriceInline(admin.StackedInline):
    model = ProductPrice
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    """Product Admin"""
    list_display = ('name', 'image',)

    inlines = [
        PriceInline,
    ]


class TagAdmin(admin.ModelAdmin):
    """Tag or category Admin"""
    list_display = ('code', 'value', 'description',)


class ProviderAdmin(admin.ModelAdmin):
    """Providers Admin"""
    list_display = ('name', 'image',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductTag, TagAdmin)
admin.site.register(Provider, ProviderAdmin)
