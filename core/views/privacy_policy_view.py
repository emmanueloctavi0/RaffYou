
# Django
from django.views.generic import TemplateView


class PrivacyPolicyView(TemplateView):
    template_name = 'core/privacy_policy.html'
