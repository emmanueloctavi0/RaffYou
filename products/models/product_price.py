
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.models import BaseModel
from products.models import Product


class ProductPrice(BaseModel):
    """The product price with their details"""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    description = models.CharField(
        _('Característica del producto'),
        max_length=150
    )

    price = models.DecimalField(
        _('Precio'),
        max_digits=6,
        decimal_places=2
    )

    hierarchy = models.IntegerField(
        _('Jerarquía'),
        default=1
    )

    def __str__(self):
        return f'{self.product.name} - {self.description} - ${self.price}'

    class Meta:
        ordering = ['hierarchy',]
        verbose_name = _('Característica de precio')
