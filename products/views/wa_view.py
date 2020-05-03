
# Django
from django.shortcuts import redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Models
from products.models import Product


@login_required
def wa_view(request, product, number):
    """Build a url whatsapp to request a product"""
    try:
        product = Product.objects.get(id=product)
    except Product.DoesNotExist:
        raise Http404('No se encontró el producto seleccionado')

    msg = (
        'Hola, Me gustaría pedir: \n'
        f'1: {product.name} \n'
        f'A la dirección: Félix Díaz #22'
    )

    url = f'https://wa.me/{number}?text={msg}'
    return redirect(url)
