
# Django
from django import forms
from django.utils.translation import gettext_lazy as _

# Models
from users.models import Address


class AddressForm(forms.ModelForm):

    references = forms.CharField(
        label=_('Ayuda al repartido a encontrar tu domicilio o el producto que necesitas'),
        min_length=15
    )

    class Meta:
        model = Address
        exclude = ['user']
