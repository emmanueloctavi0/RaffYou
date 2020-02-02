
# Django
from django.views.generic import FormView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView

# Forms
from users.forms import SignUpForm


class SignUpView(FormView):
    template_name = 'users/sign_up.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        """Call the form function save"""
        form.save()
        return super().form_valid(form)


class LoginViewCustom(LoginView):
    template_name = 'users/sign_up.html'
    success_url = '/'
