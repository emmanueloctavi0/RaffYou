
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from raffles.models import BaseModel, CatalogModelBase


class ArtistTag(CatalogModelBase):
    """Artist category or tag"""
    pass


class Artist(BaseModel):
    """Artist model. Can be an artist, band or a team"""
    name = models.CharField(
        _('Nombre'),
        max_length=100,
        unique=True
    )

    image = models.ImageField(
        upload_to='images/artists',
        blank=True
    )

    tags = models.ManyToManyField(ArtistTag)

    def __str__(self):
        return self.name
