

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.models import BaseModel
from products.models import ProductPrice
from orders.models import Order


class OrderProduct(BaseModel):
    """The talbe union between products and carts"""
    product = models.ForeignKey(
        ProductPrice,
        on_delete=models.CASCADE
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    amount = models.PositiveIntegerField(
        _('Número de productos pedidos'),
        default=1
    )

    @property
    def sub_total_price(self):
        return self.product.price * self.amount

    def __str__(self):
        return f'{self.product.product.name} - {self.amount} - ${self.sub_total_price}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'order'],
                name='unique_product_by_order'
            )
        ]
