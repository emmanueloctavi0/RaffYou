
# Django
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from products.models import BaseModel, Product

User = get_user_model()

class Cart(BaseModel):
    """Supermarket cart"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    products = models.ManyToManyField(
        Product,
        blank=True,
        through='CartProduct'
    )

    @property
    def total_price(self):
        """Cart total price"""
        return self.products.aggregate(
            models.Sum('price')
        )['price__sum'] or 0

    def __str__(self):
        return f'{self.user.email} - ${self.total_price}'



class CartProduct(BaseModel):
    """The talbe union between products and carts"""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )

    amount = models.IntegerField(
        _('Número de productos en el carrito'),
        default=1
    )

    @property
    def sub_total_price(self):
        return self.product.price * self.amount

    def __str__(self):
        return f'{self.product.name} - {self.amount} - ${self.sub_total_price}'
