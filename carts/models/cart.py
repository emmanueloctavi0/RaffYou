
# Django
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.models import BaseModel
from users.models import Address
from products.models import ProductPrice


User = get_user_model()

class Cart(BaseModel):
    """Supermarket cart"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    products = models.ManyToManyField(
        ProductPrice,
        blank=True,
        through='CartProduct'
    )

    address = models.ForeignKey(
        Address,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )

    @property
    def total_price(self):
        """Cart total price"""
        cart_products = self.cartproduct_set.all()
        price = 0
        for cart_product in cart_products:
            price += cart_product.sub_total_price
        return price

    @property
    def count_items(self):
        """Total items in the cart"""
        return self.cartproduct_set.aggregate(
            models.Sum('amount')
        )['amount__sum'] or 0

    def __str__(self):
        return f'{self.user.email} - ${self.total_price}'
