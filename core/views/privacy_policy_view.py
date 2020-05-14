
# Django
from django.views.generic import TemplateView


class PrivacyPolicyView(TemplateView):
    template_name = 'core/privacy_policy.html'


class TermsAndConditionsView(TemplateView):
    template_name = 'core/terms_and_conditions.html'
