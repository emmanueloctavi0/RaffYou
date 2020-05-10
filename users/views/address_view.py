
# Django
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

# Forms
from users.forms import AddressForm


class AddressView(LoginRequiredMixin, FormView):
    form_class = AddressForm
    template_name = 'users/address.html'
    success_url = '/'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
