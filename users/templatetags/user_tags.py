
# Django
from django import template

# Models
from users.models import Address

# Utilities
from urllib import parse

register = template.Library()


@register.simple_tag(takes_context=True)
def volando_whatsapp(context, address_id):
    """Build an url to send a whatsapp"""
    # url = 'https://wa.me/525548161007?text='
    url = 'https://wa.me/529511302570?text='
    user = context['request'].user

    cart_products = user.cart.cartproduct_set.all()
    products_text = ''

    for cart_product in cart_products:
        products_text += f'_{cart_product.amount} {cart_product.product.product.name} {cart_product.product.description}_\n'

    try:
        address = user.address_set.get(id=address_id)
        address = address.full_address
    except Address.DoesNotExist:
        address = ''

    msg = (
        f'Hola, solicito por favor: \n'
        f'{products_text}\n'
        f'*A la dirección:*\n'
        f'{address}\n'
        f'Gracias!'
    )
    msg = parse.quote(msg)
    return url + msg


@register.simple_tag(takes_context=True)
def order_whatsapp(context, product, tel):
    """Build an url to send a whatsapp"""
    tel = tel.replace(' ', '')
    url = f'https://wa.me/52{tel}?text='

    msg = (
        f'Hola, me gustaría ordenar: \n\n'
        f'{product}\n\n'
        f'¡Gracias!'
    )
    msg = parse.quote(msg)

    return url + msg
