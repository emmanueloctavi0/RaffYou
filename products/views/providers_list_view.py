
# Django
from django.views.generic import ListView
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError

# Models
from products.models import Provider

# Utilities
from core.utils import random_pk_list


class ProviderListView(ListView):
    model = Provider
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(
            image=''
        ).order_by('-created_at')

        try:
            query = self.request.GET['q']
        except MultiValueDictKeyError:
            return queryset

        return queryset.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
