
# Django
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class SignUpForm(forms.ModelForm):
    """Register a new user"""
    password_confirmation = forms.CharField(
        label=_('Confirma tu contraseña'),
        min_length=8,
        widget=forms.TextInput(attrs={
            'type': 'password'
        })
    )

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        ]
    