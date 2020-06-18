
# Django
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Product

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
