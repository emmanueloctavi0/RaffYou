
# Django REST Framework
from rest_framework import generics, viewsets

# Serializers
from carts.serializers import CartProductSerializer

# Models
from carts.models import CartProduct


class CartProductViewSet(viewsets.ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer
