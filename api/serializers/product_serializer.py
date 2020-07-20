
# Django REST Framework
from rest_framework import serializers

# Models
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = [
            'created_at',
            'updated_at',
            # 'tags',
            'is_active'
        ]

    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='value'
    )

    provider = serializers.StringRelatedField()
