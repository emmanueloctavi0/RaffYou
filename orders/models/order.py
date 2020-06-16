
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models
from core.models import BaseModel, AddressBaseModel
from users.models import Address
from products.models import ProductPrice
from django.contrib.auth import get_user_model

# Task
from core.tasks import send_email_html


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

    comment = models.TextField(
        _('Comentarios adicionales'),
        max_length=300,
        blank=True,
    )

    @property
    def total_price(self):
        """Cart total price"""
        order_products = self.orderproduct_set.all()
        price = 0
        for order_product in order_products:
            price += order_product.sub_total_price
        return price

    def __str__(self):
        return f'{self.address.telephone} {self.products.first()}...'

    class Meta:
        verbose_name = _('Pedido')
        verbose_name_plural = _('Pedidos')


@receiver(post_save, sender=Order)
def handler_status(sender, instance, **kwargs):
    """Send an email when the order status change"""
    from_email = 'Equipo RaffYou'
    recipient_list = [instance.user.email]
    if instance.status == Order.Status.STARTED.value:
        subject = '¡Recibimos tu pedido!'
        template = 'mails/order_received.html'
    elif instance.status == Order.Status.FINISHED.value:
        subject = '¡Entregamos tu pedido!'
        template = 'mails/order_success.html'
    elif instance.status == Order.Status.ON_WAY.value:
        subject = '¡Tu pedido va en camino!'
        template = 'mails/order_sent.html'
    elif instance.status == Order.Status.CANCELLED.value:
        subject = 'Tu pedido ha sido cancelado :C'
        template = 'mails/order_cancel.html'
    else:
        return

    send_email_html.delay(
        subject,
        template,
        from_email,
        recipient_list
    )
