
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from raffles.models import BaseModel


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
        upload_to='media/images/raffles'    ,
        blank=True
    )

    def __str__(self):
        return self.name
