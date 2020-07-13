
# Django REST Framework
from rest_framework.generics import ListAPIView

# Serializers
from api.serializers import ProductSerializer

# Models
from products.models import Product


class ProductAPIView(ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = []