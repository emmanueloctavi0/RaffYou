
# Django
from django.contrib import admin
from django.shortcuts import reverse

# Models
from products.models import (
    Product, ProductTag, ProductPrice,
    Provider, ProviderAddress, ScheduleDay
)

# Utilities
from django.utils.html import format_html


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


class ScheduleDayInline(admin.TabularInline):
    model = ScheduleDay
    extra = 0


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

    fields = (
        'product_detail',
        'name',
        'image',
        'keywords',
        'is_active',
    )

    list_display_links = ('name', )

    readonly_fields = ('product_detail', 'image', )

    def product_detail(self, obj):
        product_detail_url = reverse('admin:products_product_change', args=[obj.id])
        return format_html(
            '<a target="_blank" href="{}">{}</a>',
            product_detail_url,
            obj.id,
        )


class ProviderAdmin(admin.ModelAdmin):
    """Providers Admin"""
    list_display = ('name', 'image', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('name', 'description', 'keywords',)

    inlines = [
        ProductInline,
        ProviderAddressInline,
        ScheduleDayInline,
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductTag, TagAdmin)
admin.site.register(Provider, ProviderAdmin)
