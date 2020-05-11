
# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def cart_address_view(request):
    """Select the address to send the order"""
    addresses = request.user.address_set.all()
    return render(
        request,
        'carts/cart_address.html',
        context={
            'addresses': addresses,
        }
    )
