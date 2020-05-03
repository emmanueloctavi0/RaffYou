
# Django
from django.views.generic.detail import DetailView

from products.models import Product

class ProductDetailView(DetailView):
    model = Product
