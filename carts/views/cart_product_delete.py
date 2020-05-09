
# Django
from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Models
from carts.models import CartProduct, Cart


@login_required
def cart_product_delete_view(request, cart_product):
    """Delete a product from user cart"""
    if request.method != 'POST':
        return HttpResponseNotAllowed(permitted_methods=['POST',])

    try:
        cart_product = request.user.cart.cartproduct_set.get(id=cart_product)
        cart_product.delete()
    except (CartProduct.DoesNotExist, Cart.DoesNotExist):
        pass
    return redirect('carts:index')
