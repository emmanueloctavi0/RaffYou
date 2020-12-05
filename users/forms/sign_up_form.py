
# Django
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail


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

    def send_mail_confirmation(self):
        """
        Send mail email confirmation
        """
        data = self.cleaned_data
        email = data.get('email')
        username = data.get('first_name')
        msg = (
            'Hola {}, da click al siguiente enlace para confirmar tu cuenta! \n'
            'Link: https://raffyou.com/confirmation/?id=adsfasdfSDJFJsmmffkwosl34m2n3'
        ).format(username)

        send_mail(
            'Confirma tu correo en RaffYou',
            msg,
            'no-reply@raffyou.com',
            [email],
            fail_silently=False,
        )
