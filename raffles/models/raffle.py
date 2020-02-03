
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from raffles.models import BaseModel, Artist


class Raffle(BaseModel):
    """Raffle model"""
    name = models.CharField(
        _('Nombre'),
        max_length=250
    )

    description = models.TextField(
        _('Descripción'),
        blank=True
    )

    image = models.ImageField(
        upload_to='images/raffles',
        blank=True
    )

    event_date = models.DateTimeField(
        _('Fecha del evento')
    )

    event_address = models.CharField(
        _('Lugar del evento'),
        max_length=250
    )

    price = models.DecimalField(
        _('Precio'),
        max_digits=3,
        decimal_places=1
    )

    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return self.name
