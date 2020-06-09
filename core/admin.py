
# Django
from django.contrib.admin import AdminSite

# Models
from orders.models import Order


class RaffyouAdminSite(AdminSite):
    site_header = 'RaffYou Administrador'

    def each_context(self, request):
        context = super().each_context(request)
        context['orders_count'] = Order.objects.filter(
            status=1
        ).count()
        return context
        
admin_site = RaffyouAdminSite(name='raffyou_admin')
