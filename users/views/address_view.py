
# Django
from django.views.generic import FormView

# Forms
from users.forms import AddressForm


class AddressView(FormView):
    form_class = AddressForm
    template_name = 'users/address.html'
