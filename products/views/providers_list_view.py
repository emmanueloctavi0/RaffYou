
# Django
from django.views.generic import ListView
from django.db.models import Q, Avg, Min
from django.utils.datastructures import MultiValueDictKeyError

# Models
from products.models import Provider, Product

# Utilities
from core.utils import random_pk_list


class ProviderListView(ListView):
    model = Provider
    paginate_by = 25
    queryset = Provider.objects.filter(is_active=True)

    def get_context_data(self):
        context = super().get_context_data()
        context['products'] = Product.objects.filter(
            is_active=True
        ).exclude(
            image=''
        ).values(
            'id', 'name', 'image', 'provider__id',
            'provider__name', 'price_default'
        ).annotate(Min('productprice__hierarchy'))[:3]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(
            image=''
        )

        try:
            query = self.request.GET['q']
        except MultiValueDictKeyError:
            return queryset.values(
            'id', 'image', 'name',
            'description',
        ).annotate(Avg('score__rate'))

        return queryset.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        ).values(
            'id', 'image', 'name',
            'description',
        ).annotate(Avg('score__rate'))
