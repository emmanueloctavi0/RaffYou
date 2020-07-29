
# Django
from django.views.generic import ListView
from django.db.models import Q, Min, Avg
from django.utils.datastructures import MultiValueDictKeyError

# Models
from products.models import Product, Provider, ProductPrice, ProductTag

# Utilities
from core.utils import random_pk_list


class ProductsHomeView(ListView):
    model = Product
    paginate_by = 6
    queryset = Product.objects.filter(is_active=True)
    queryset_provider = Provider.objects.filter(is_active=True)

    def get_queryset(self):
        queryset = super().get_queryset()

        try:
            query = self.request.GET['q']
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(tags__value__icontains=query) |
                Q(tags__description__icontains=query) |
                Q(description__icontains=query) |
                Q(keywords__icontains=query)
            )
        except MultiValueDictKeyError:
            pass

        queryset = queryset.values(
            'id', 'name', 'image', 'provider__id',
            'provider__name', 'price_default'
        ).annotate(Min('productprice__hierarchy'))

        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        query = self.request.GET.get('q')
        providers = self.queryset_provider.values(
            'id', 'image', 'name',
            'description',
        ).annotate(Avg('score__rate'))
        context['categories'] = ProductTag.objects.all().values(
            'id', 'value'
        )

        if query:
            context['search'] = f'q={query}'
            context['providers'] = providers.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(keywords__icontains=query)
            )[:3]
        else:
            context['providers'] = providers[:3]

        return context
