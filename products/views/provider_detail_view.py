
# Django
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.core.paginator import Paginator

# Models
from products.models import Provider, Score, Product

# Forms
from products.forms import ScoreForm

# Utilities
from django.db import IntegrityError


class ProviderDetailView(DetailView):
    model = Provider
    queryset_product = Product.objects.filter(is_active=True)
    queryset = Provider.objects.filter(is_active=True)

    def get_products_list(self):
        """
        Get the products from provider with a paginator
        """
        products = self.queryset_product
        products = products.filter(
            provider=self.get_object()
        )
        paginator = Paginator(products, 3) # Show 25 contacts per page.

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return page_obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['score_form'] = ScoreForm()
        context['page_obj'] = self.get_products_list()
        context['is_paginated'] = True
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        score_form = ScoreForm(request.POST)
        if score_form.is_valid():
            try:
                score_form.instance.user = request.user
                score_form.instance.provider = self.object
                score_form.save()
                messages.success(request, '¡Tu comentario se ha agreado exitosamente!')
            except IntegrityError:
                score = Score.objects.get(
                    user=request.user,
                    provider=self.object
                )
                score_form.instance.id = score.id
                score_form.save()
                messages.success(request, '¡Tu comentario se ha actualizado exitosamente!')
        else:
            context = self.get_context_data(object=self.object)
            context['score_form'] = score_form
            for error in score_form.errors.keys():
                msg = score_form.errors[error]
                messages.error(request, msg[0])
            return self.render_to_response(context)
        return self.get(request, args, kwargs)
