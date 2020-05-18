
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.models import BaseModel
from users.models import Address
from products.models import ProductPrice
from django.contrib.auth import get_user_model


User = get_user_model()


class Order(BaseModel):
    """The order model"""

    class Status(models.IntegerChoices):
        STARTED = 1, _('En camino')
        FINISHED = 2, _('Entregado / Pagado')
        CANCELLED = 3, _('Cancelado')

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True
    )

    address = models.ForeignKey(
        Address,
        on_delete=models.DO_NOTHING,
        null=True
    )

    products = models.ManyToManyField(
        ProductPrice
    )

    status = models.IntegerField(
        _('Estatus del pedido'),
        choices=Status.choices,
        default=Status.STARTED,
    )
