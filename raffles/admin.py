
# Django
from django.contrib import admin

# Models
from raffles.models import Raffle, ArtistTag, Artist


class RaffleAdmin(admin.ModelAdmin):
    """Raffle Admin"""
    list_display = ('name', 'event_date', 'event_address', 'image',)


class TagAdmin(admin.ModelAdmin):
    """Tag or category Admin"""
    list_display = ('code', 'value', 'description',)


class ArtistAdmin(admin.ModelAdmin):
    """Artists Admin"""
    list_display = ('name', 'image',)


admin.site.register(Raffle, RaffleAdmin)
admin.site.register(ArtistTag, TagAdmin)
admin.site.register(Artist, ArtistAdmin)
