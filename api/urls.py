
# Django
from django.urls import path

# Views
from api import views


urlpatterns = [
    path('products/', views.ProductAPIView.as_view()),
    path('providers/', views.ProviderAPIView.as_view()),
]
