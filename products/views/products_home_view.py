
# Django
from django.views.generic import ListView
from django.shortcuts import redirect

# Models
from products.models import Product


class ProductsHomeView(ListView):
    template_name = 'products/home.html'
    model = Product
    paginate_by = 3


def redirect_home_view(request):
    return redirect('products:home')
