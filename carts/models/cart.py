
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

    amount = models.PositiveIntegerField(
        _('Número de productos en el carrito'),
        default=1
    )

    @property
    def sub_total_price(self):
        return self.product.price * self.amount

    def __str__(self):
        return f'{self.product.name} - {self.amount} - ${self.sub_total_price}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'cart'],
                name='unique_product_by_cart'
            )
        ]
