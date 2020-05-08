
# Django REST Framework
from rest_framework import generics, viewsets

# Serializers
from carts.serializers import CartProductSerializer

# Models
from carts.models import CartProduct, Cart

# Utilities
from django.db import IntegrityError


class CartProductViewSet(viewsets.ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    def get_queryset(self):
        """Only permit list the cart_product of users loged"""
        queryset = super().get_queryset()
        queryset = queryset.filter(
            cart__user=self.request.user
        )
        return queryset

    def perform_create(self, serializer):
        """Add the product to the cart"""
        try:
            serializer.save(cart=self.request.user.cart)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                user=self.request.user,
            )
            serializer.save(cart=cart)
        except IntegrityError:
            product = serializer.validated_data['product']
            cart_product = self.request.user.cart.cartproduct_set.get(
                product=product
            )
            amount = serializer.validated_data.get('amount')
            if amount:
                cart_product.amount = amount
            else:
                cart_product.amount += 1
            serializer.instance = cart_product
            serializer.save()
