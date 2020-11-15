# Django
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from users.models import Address

class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    paginate_by = 3

    def get_queryset(self):
        return Address.objects.filter(
            user=self.request.user
        )
