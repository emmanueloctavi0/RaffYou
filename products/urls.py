
# Django
from django.urls import path

# Views
from products import views


app_name = 'products'

urlpatterns = [
    path('', views.ProductsHomeView.as_view(), name='home'),
]
