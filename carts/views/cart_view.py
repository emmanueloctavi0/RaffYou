
# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def cart_view(request):
    """Cart view"""
    cart_products = request.user.cart.cartproduct_set.all()
    return render(request, 'carts/cart.html', {
        'cart_products': cart_products,
    })
