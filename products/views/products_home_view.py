
# Django
from django.views.generic import ListView
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError

# Models
from products.models import Product, Provider

# Utilities
from core.utils import random_pk_list


class ProductsHomeView(ListView):
    model = Product
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-created_at')
        try:
            query = self.request.GET['q']
        except MultiValueDictKeyError:
            return queryset

        return queryset.filter(
            Q(name__icontains=query) |
            Q(tags__value__icontains=query) |
            Q(tags__description__icontains=query) |
            Q(description__icontains=query)
        )

    def get_context_data(self):
        context = super().get_context_data()
        context['providers'] = Provider.objects.filter(
            id__in=random_pk_list(Provider, 5),
        ).exclude(
            image=''
        )

        return context
