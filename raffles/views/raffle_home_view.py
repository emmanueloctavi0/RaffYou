
# Django
from django.views.generic import TemplateView
from django.shortcuts import redirect

# Models
from raffles.models import Raffle


class RaffleHomeView(TemplateView):
    template_name = 'raffles/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['raffles'] = Raffle.objects.all()
        return context


def redirect_home_view(request):
    return redirect('raffles:home')
