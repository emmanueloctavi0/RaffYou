# Django
from django.views.generic import TemplateView


class OrderHelpView(TemplateView):
    template_name = 'orders/order_help.html'
