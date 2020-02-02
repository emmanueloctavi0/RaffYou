
# Django
from django.contrib import admin

# Models
from raffles.models import Raffle


class RaffleAdmin(admin.ModelAdmin):
    """Raffle Admin"""
    list_display = ('name', 'event_date', 'event_address', 'image',)


admin.site.register(Raffle, RaffleAdmin)
