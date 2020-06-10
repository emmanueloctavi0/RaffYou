
# Django
from django.views.generic import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.forms.models import model_to_dict

# Models
from carts.models import Cart
from orders.models import Order, OrderProduct, OrderAddress

# Tasks
from carts.tasks import create_order


class CartResumeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        try:
            cart_products = request.user.cart.cartproduct_set.all()
            cart = request.user.cart
        except Cart.DoesNotExist:
            return redirect('carts:index')

        return render(
            request,
            'carts/cart_resume.html',
            context={
                'cart_products': cart_products,
                'cart': cart,
            }
        )

    def post(self, request):
        try:
            cart = request.user.cart
        except Cart.DoesNotExist:
            return redirect('carts:index')

        # Address order
        order_address = model_to_dict(cart.address)
        order_address.pop('user')
        order_address.pop('id')

        # Create order
        create_order.delay(
            order_address,
            request.user.id,
            cart.id,
            request.POST.get('comment', '')
        )

        # Send messages
        order_url = reverse('orders:order-list')
        messages.success(
            request,
            ('!Tu pedido ha sido solicitado!. '
            'Visita la sección '
            f'<a href="{order_url}"><strong>Mis pedidos</strong></a> '
            'para conocer el estatus de tus solicitudes')
        )

        return redirect('products:home')
