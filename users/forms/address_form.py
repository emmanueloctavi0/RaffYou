
# Django
from django import forms

# Models
from users.models import Address


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = '__all__'
