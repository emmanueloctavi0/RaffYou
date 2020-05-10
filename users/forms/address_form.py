
# Django
from django import forms
from django.utils.translation import gettext_lazy as _

# Models
from users.models import Address


class AddressForm(forms.ModelForm):

    references = forms.CharField(
        label=_('Indicaciones adicionales para entregar tus compras en esta dirección'),
        min_length=15
    )

    class Meta:
        model = Address
        exclude = ['user']
