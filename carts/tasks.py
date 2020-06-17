from __future__ import absolute_import, unicode_literals

from celery import shared_task

# Models
from orders.models import OrderAddress, Order, OrderProduct
from carts.models import Cart, PromotionalCode

# Task
from core.tasks import send_email_text

# Utilities
from carts.utils import check_code


@shared_task
def create_order(address_dict, user_id, cart_id, comment, code=''):
    """Create a user order"""
    order_address = OrderAddress.objects.create(**address_dict)

    order = Order.objects.create(
        user_id=user_id,
        address=order_address,
        comment=comment,
        shipping_price=15
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

    if is_valid:
        p_code = PromotionalCode.objects.get(code=code)
        p_code.update_use()

    send_email_text.delay(
        'Nuevo pedido en RaffYou',
        'Hay un pedido en RaffYou, entra a https://raffyou.com/admin/',
        'support@raffyou.com',
        [
            'emmanueloctaviomc@gmail.com',
            'chavi.sennin@gmail.com',
            'luisescorpions79@gmail.com',
        ],
    )

    return {
        'user_id': user_id,
        'order_id': order.id,
    }
