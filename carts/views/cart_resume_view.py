
# Django
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class CartResumeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        cart_products = request.user.cart.cartproduct_set.all()
        cart = request.user.cart

        return render(
            request,
            'carts/cart_resume.html',
            context={
                'cart_products': cart_products,
                'cart': cart,
            }
        )
