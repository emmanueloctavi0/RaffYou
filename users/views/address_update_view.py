
# Django
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from users.models import Address

# Forms
from users.forms import AddressForm


class AddressUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/address.html'
    form_class = AddressForm
    success_url = reverse_lazy('users:address-list')

    def get_queryset(self):
        return Address.objects.filter(
            user=self.request.user
        )

    def get_success_url(self):
        """If exists param 'next' redirect to tha path"""
        return self.request.GET.get(
            'next',
            super().get_success_url()
        )
