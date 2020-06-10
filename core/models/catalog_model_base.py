
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.models import BaseModel


class CatalogModelBase(BaseModel):
    """Catalog model base"""
    code = models.CharField(
        _('Código'),
        max_length=30,
        unique=True
    )
    value = models.CharField(
        _('Nombre'),
        max_length=100
    )

    description = models.CharField(
        _('Descripción'),
        max_length=250,
        blank=True
    )

    def __str__(self):
        return '{} - {}'.format(self.code, self.value)

    class Meta:
        abstract = True
