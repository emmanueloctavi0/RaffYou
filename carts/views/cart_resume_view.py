
# Django
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from carts.models import Cart


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
