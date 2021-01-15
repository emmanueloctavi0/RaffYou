
# Django
from django.urls import path

# Views
from core import views


app_name = 'core'


urlpatterns = [
    path('', views.redirect_home_view, name='redirect-home'),
    path('miprivacidad/', views.PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('terminos/', views.TermsAndConditionsView.as_view(), name='terms-policy'),
    path('registro/', views.LandingPageView.as_view(), name='core-formulary'),
]
