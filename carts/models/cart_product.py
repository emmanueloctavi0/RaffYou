
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.models import BaseModel
from products.models import ProductPrice
from carts.models import Cart


class CartProduct(BaseModel):
    """The talbe union between products and carts"""
    product = models.ForeignKey(
        ProductPrice,
        on_delete=models.CASCADE
    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )

    amount = models.PositiveIntegerField(
        _('Número de productos en el carrito'),
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
                fields=['product', 'cart'],
                name='unique_product_by_cart'
            )
        ]
