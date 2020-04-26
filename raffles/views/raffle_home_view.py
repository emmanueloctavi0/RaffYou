
# Django
from django.views.generic import ListView
from django.shortcuts import redirect

# Models
from raffles.models import Raffle


class RaffleHomeView(ListView):
    template_name = 'raffles/home.html'
    model = Raffle
    paginate_by = 3


def redirect_home_view(request):
    return redirect('raffles:home')
