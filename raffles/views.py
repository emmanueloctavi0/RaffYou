from django.views.generic import TemplateView


class RaffleHomeView(TemplateView):
    template_name = 'raffles/home.html'
