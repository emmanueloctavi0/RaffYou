
# Django
from django.views.generic import TemplateView
from django.shortcuts import redirect


class RaffleHomeView(TemplateView):
    template_name = 'raffles/home.html'


def redirect_home_view(request):
    return redirect('raffles:home')
