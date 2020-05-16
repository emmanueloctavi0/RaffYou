
# Django
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class CartResumeView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'carts/cart_resume.html')
