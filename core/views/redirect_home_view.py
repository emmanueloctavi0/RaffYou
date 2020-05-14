
# Django
from django.shortcuts import redirect


def redirect_home_view(request):
    return redirect('products:home')
