
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Models
from core.models import BaseModel, AddressBaseModel
from users.models import Address
from products.models import ProductPrice
from django.contrib.auth import get_user_model


User = get_user_model()


class OrderAddress(AddressBaseModel):
    def __str__(self):
        return f'{self.name} - {self.zip_code}'


class Order(BaseModel):
    """The order model"""

    class Status(models.IntegerChoices):
        STARTED = 1, _('Solicitado')
        ON_WAY = 2, _('En camino')
        FINISHED = 3, _('Entregado / Pagado')
        CANCELLED = 4, _('Cancelado')

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True
    )

    address = models.OneToOneField(
        OrderAddress,
        on_delete=models.DO_NOTHING,
        null=True
    )

    products = models.ManyToManyField(
        ProductPrice,
        through='OrderProduct'
    )

    status = models.IntegerField(
        _('Estatus del pedido'),
        choices=Status.choices,
        default=Status.STARTED,
    )

    def __str__(self):
        return f'{self.address.telephone} {self.products.first()}...'

    class Meta:
        verbose_name = _('Pedido')
        verbose_name_plural = _('Pedidos')
