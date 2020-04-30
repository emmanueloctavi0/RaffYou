
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from products.models import BaseModel, CatalogModelBase


class Provider(BaseModel):
    """Provider model. A provider"""
    name = models.CharField(
        _('Nombre'),
        max_length=100,
        unique=True
    )

    description = models.TextField(
        _('Descripción'),
        blank=True
    )

    image = models.ImageField(
        upload_to='images/providers',
        blank=True
    )

    def __str__(self):
        return self.name
