
# Django REST Framework
from rest_framework import generics, viewsets

# Serializers
from carts.serializers import CartProductSerializer

# Models
from carts.models import CartProduct


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
        serializer.save(cart=self.request.user.cart)
