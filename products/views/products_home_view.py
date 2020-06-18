
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
    paginate_by = 6
    ordering = ['created_at']
    queryset = Product.objects.filter(is_active=True)
    queryset_provider = Provider.objects.filter(is_active=True)

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')

        try:
            query = self.request.GET['q']
        except MultiValueDictKeyError:
            return queryset

        return queryset.filter(
            Q(name__icontains=query) |
            Q(tags__value__icontains=query) |
            Q(tags__description__icontains=query) |
            Q(description__icontains=query) |
            Q(keywords__icontains=query)
        )

    def get_context_data(self):
        context = super().get_context_data()
        query = self.request.GET.get('q')
        providers = self.queryset_provider

        if query:
            context['search'] = f'q={query}'
            context['providers'] = providers.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(keywords__icontains=query)
            )[:3]
        else:
            context['providers'] = providers.filter(
                id__in=random_pk_list(Provider, 3),
            )

        return context
