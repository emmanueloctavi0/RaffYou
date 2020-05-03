
# Django
from django.views.generic import ListView
from django.shortcuts import redirect
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError

# Models
from products.models import Product


class ProductsHomeView(ListView):
    model = Product
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
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


def redirect_home_view(request):
    return redirect('products:home')
