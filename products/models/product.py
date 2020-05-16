
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from products.models import Provider
from core.models import BaseModel, CatalogModelBase


class ProductTag(CatalogModelBase):
    """Provider category or tag"""
    pass


class Product(BaseModel):
    """Product model"""
    name = models.CharField(
        _('Nombre'),
        max_length=250
    )

    description = models.TextField(
        _('Descripción'),
        blank=True
    )

    image = models.ImageField(
        upload_to='images/products',
        blank=True
    )

    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    tags = models.ManyToManyField(ProductTag, blank=True)

    def __str__(self):
        return self.name
