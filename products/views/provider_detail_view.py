
# Django
from django.views.generic import DetailView

# Models
from products.models import Provider


class ProviderDetailView(DetailView):
    model = Provider
