
# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Models
from carts.models import Cart
from products.models import Product


@login_required
def cart_view(request):
    """Cart view"""
    try:
        cart_products = request.user.cart.cartproduct_set.all()
    except Cart.DoesNotExist:
        cart_products = None

    products = Product.objects.all()

    return render(request, 'carts/cart.html', {
        'cart_products': cart_products,
        'products': products,
    })
