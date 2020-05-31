
# Django
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.forms.models import model_to_dict

# Models
from carts.models import Cart
from orders.models import Order, OrderProduct, OrderAddress


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
            cart_products = request.user.cart.cartproduct_set.all()
            cart = request.user.cart
        except Cart.DoesNotExist:
            return redirect('carts:index')
        
        # Address order
        order_address = model_to_dict(cart.address)
        order_address.pop('user')
        order_address.pop('id')
        order_address = OrderAddress.objects.create(**order_address)

        # Create order
        order = Order.objects.create(
            user=request.user,
            address=order_address,
            comment=request.POST.get('comment', '')
        )

        # Set order products
        for cart_product in cart_products:
            order_product = OrderProduct.objects.create(
                order=order,
                product=cart_product.product,
                amount=cart_product.amount,
            )
        cart.delete()

        messages.success(request, '!Tu pedido ha sido solicitado!')
        return redirect('orders:order-list')
