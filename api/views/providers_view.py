
# Django REST Framework
from rest_framework.generics import ListAPIView

# Serializers
from api.serializers import ProviderSerializer

# Models
from products.models import Provider


class ProviderAPIView(ListAPIView):
    queryset = Provider.objects.filter(is_active=True)
    serializer_class = ProviderSerializer
    permission_classes = []
