
# Django
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Forms
from users.forms import AddressForm


class AddressCreateView(LoginRequiredMixin, FormView):
    form_class = AddressForm
    template_name = 'users/address.html'
    success_url = reverse_lazy('users:address-list')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
