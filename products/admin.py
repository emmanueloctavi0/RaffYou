
# Django
from django.contrib import admin

# Models
from products.models import (
    Product, ProductTag, ProductPrice,
    Provider, ProviderAddress
)


class PriceInline(admin.StackedInline):
    model = ProductPrice
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    """Product Admin"""
    list_display = ('name', 'image', 'provider', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'provider')
    search_fields = ('name', 'description', 'keywords',)

    inlines = [
        PriceInline,
    ]


class TagAdmin(admin.ModelAdmin):
    """Tag or category Admin"""
    list_display = ('code', 'value', 'description',)


class ProviderAddressInline(admin.StackedInline):
    model = ProviderAddress
    extra = 0


class ProviderAdmin(admin.ModelAdmin):
    """Providers Admin"""
    list_display = ('name', 'image', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('name', 'description', 'keywords',)

    inlines = [
        ProviderAddressInline,
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductTag, TagAdmin)
admin.site.register(Provider, ProviderAdmin)
