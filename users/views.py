
# Django
from django.views.generic import FormView
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Forms
from users.forms import SignUpForm


class SignUpView(FormView):
    template_name = 'users/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('raffles:home')

    def form_valid(self, form):
        """Call the form function save"""
        form.save()
        # form.send_mail_confirmation()
        return super().form_valid(form)


class LoginViewCustom(LoginView):
    template_name = 'users/sign_up.html'
    success_url = reverse_lazy('raffles:home')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('raffles:home')
