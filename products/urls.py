
# Django
from django.urls import path

# Views
from products import views


app_name = 'products'

urlpatterns = [
    path('', views.ProductsHomeView.as_view(), name='home'),
    path('negocio/<int:pk>/', views.ProviderDetailView.as_view(), name='provider-detail'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('pedir/<int:product>/<number>/', views.wa_view, name='wa_view'),
]
