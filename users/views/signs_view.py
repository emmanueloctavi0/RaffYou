
# Django
from django.views.generic import FormView, TemplateView
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Forms
from users.forms import SignUpForm


class SignUpView(FormView):
    template_name = 'users/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('products:home')

    def form_valid(self, form):
        """Call the form function save"""
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginViewCustom(LoginView):
    template_name = 'users/login.html'


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('products:home')
