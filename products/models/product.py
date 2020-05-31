
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from products.models import Provider
from core.models import BaseModel, CatalogModelBase


class ProductTag(CatalogModelBase):
    """Provider category or tag"""

    class Meta:
        verbose_name = _('Categoría de producto')
        verbose_name_plural = _('Categorias de productos')


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

    keywords = models.CharField(
        _('Palabras clave de búsqueda'),
        max_length=255,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Producto')
        verbose_name_plural = _('Productos')
