
# Django
from django.contrib import admin

# Models
from raffles.models import Raffle


class RaffleAdmin(admin.ModelAdmin):
    """Raffle Admin"""
    pass


admin.site.register(Raffle, RaffleAdmin)
