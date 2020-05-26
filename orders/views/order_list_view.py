
# Django
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from orders.models import Order


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    paginate_by = 3
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user=self.request.user
        ).order_by(
            '-updated_at',
        )
