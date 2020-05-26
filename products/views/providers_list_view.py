
# Django
from django.views.generic import ListView
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError

# Models
from products.models import Provider, Product

# Utilities
from core.utils import random_pk_list


class ProviderListView(ListView):
    model = Provider
    paginate_by = 6

    def get_context_data(self):
        context = super().get_context_data()
        context['products'] = Product.objects.filter(
            id__in=random_pk_list(Product, 3)
        ).exclude(
            image=''
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(
            image=''
        ).order_by('?')

        try:
            query = self.request.GET['q']
        except MultiValueDictKeyError:
            return queryset

        return queryset.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
