
# Django
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Models
from users.models import Address


class CartAddressView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        """Select the address to send the order"""
        addresses = request.user.address_set.all()
        return render(
            request,
            'carts/cart_address.html',
            context={
                'addresses': addresses,
            }
        )

    def post(self, request):
        try:
            address = request.user.address_set.get(
                id=request.POST.get('address')
            )
        except Address.DoesNotExist:
            addresses = request.user.address_set.all()
            return render(
                request,
                'carts/cart_address.html',
                context={
                    'addresses': addresses,
                }
            )
        request.user.cart.address = address
        request.user.cart.save()
        return redirect('carts:cart-resume')
