
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

    address = models.CharField(
        _('Dirección de venta del producto'),
        max_length=250
    )

    price = models.DecimalField(
        _('Precio'),
        max_digits=6,
        decimal_places=2
    )

    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE
    )

    tags = models.ManyToManyField(ProductTag)

    def __str__(self):
        return self.name
