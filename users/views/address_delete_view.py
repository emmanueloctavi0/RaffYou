
# Django
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from users.models import Address


class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    success_url = reverse_lazy('users:address-list')

    def get_queryset(self):
        return Address.objects.filter(
            user=self.request.user
        )
