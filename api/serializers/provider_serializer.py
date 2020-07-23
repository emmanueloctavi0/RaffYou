
# Django REST Framework
from rest_framework import serializers

# Models
from products.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        exclude = [
            'created_at',
            'updated_at',
            'is_active',
        ]
