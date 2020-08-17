from __future__ import absolute_import, unicode_literals

from celery import shared_task

# Models
from orders.models import OrderAddress, Order, OrderProduct
from carts.models import Cart, PromotionalCode

# Task
from core.tasks import send_telegram_message

# Utilities
from carts.utils import check_code
from core.utils import clean_word
import requests


def parse_message(order):

    text = (
        f'Nuevo pedido:\n'
        f'*[Orden \#{order.id}](https://raffyou.com/admin/orders/order/)*\n\n'

        f'*Solicitante:* {clean_word(order.address.name)}\n'
        f'*Teléfono:* [{clean_word(order.address.telephone)}](https://wa.me/52{order.address.clean_telephone}?text=Hola)\n'
        f'*Calle:* {clean_word(order.address.street_name)}\n'
        f'*Número:* {clean_word(order.address.street_number)}\n'
        f'*Barrio/Colonia:* {clean_word(order.address.colony)}\n'
        f'*Referencia de la dirección:* {clean_word(order.address.references)}\n'
        f'*Comentarios del pedido:* {clean_word(order.comment)}\n'
        f'*Solicita:* \n'
    )

    for product in order.orderproduct_set.all():
        provider = product.product.product.provider
        provider_url = f'https://raffyou.com/comida/negocio/{provider.id}/'
        telephone = provider.provideraddress_set.first().clean_telephone
        telephone = clean_word(telephone)

        provider_phone = f'[{telephone}](https://wa.me/52{telephone}?text=Hola)'

        product_text = clean_word(product.__str__())
        text += f'    \-{product_text}\. [{clean_word(provider.name)}]({provider_url}) Tel: {provider_phone}\n'

    price = str(order.price)
    text += (
        f'\n*Precio con el envío:* ${clean_word(price)}'
    )

    return text


@shared_task
def create_order(address_dict, user_id, cart_id, comment, code=''):
    """Create a user order"""
    order_address = OrderAddress.objects.create(**address_dict)

    order = Order.objects.create(
        user_id=user_id,
        address=order_address,
        comment=comment,
        shipping_price=20
    )

    cart = Cart.objects.get(id=cart_id)
    cart_products = cart.cartproduct_set.all()

    # Set order products
    for cart_product in cart_products:
        order_product = OrderProduct.objects.create(
            order=order,
            product=cart_product.product,
            amount=cart_product.amount,
        )

    # Set the price and discount if exists
    order.price = order.price_calc
    is_valid, total_price = check_code(code, order.price)
    order.total_price = total_price
    order.save()
    cart.delete()

    if is_valid:
        p_code = PromotionalCode.objects.get(code=code)
        p_code.update_use()

    send_telegram_message.delay(parse_message(order))

    return {
        'user_id': user_id,
        'order_id': order.id,
    }
