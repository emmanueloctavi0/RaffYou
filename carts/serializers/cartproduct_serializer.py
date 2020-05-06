
# Django REST Framework
from rest_framework import serializers

# Models
from carts.models import CartProduct


class CartProductSerializer(serializers.ModelSerializer):
    """Cart serializer"""
    class Meta:
        model = CartProduct
        fields = '__all__'
