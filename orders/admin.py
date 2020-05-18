
# Django
from django.contrib import admin

# Models
from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)