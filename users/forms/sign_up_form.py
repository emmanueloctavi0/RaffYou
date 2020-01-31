
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

    password = forms.CharField(
        label=_('Contraseña'),
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

    def clean(self):
        """Verify password confirmation match"""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            msg = _('Las contraseñas no coinciden')
            self.add_error('password', msg)

        return cleaned_data

    def save(self, commit=True):
        """
        Set user password
        """
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return user
