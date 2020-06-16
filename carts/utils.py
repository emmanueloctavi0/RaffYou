
# Django
from carts.models import PromotionalCode

# Utilities
import datetime


def check_code(code, price):
    """
    Verify the promotional code, if is valid return True and the new price
    """
    try:
        promotional_code = PromotionalCode.objects.get(
            code=code,
            is_active=True,
            expiry_datetime__gte=datetime.datetime.now()
        )
    except PromotionalCode.DoesNotExist:
        return False, price

    # Make the discount
    mount = promotional_code.discount_mount

    if promotional_code.cart_discount == 'FIXED':
        price = price - mount
    elif promotional_code.cart_discount == 'PERC':
        discount = price * mount / 100
        price = price - discount
    elif promotional_code.cart_discount == 'FREE':
        price = 0
    else:
        return False, price

    if price < 0:
        price = 0

    return True, price
