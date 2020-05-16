
# Django
from django.urls import include, path

# Django REST Framework
from rest_framework import routers

# Views
from carts import views

router = routers.DefaultRouter()
router.register('products', views.CartProductViewSet)

app_name = 'carts'


urlpatterns = [
    path('', views.cart_view, name='index'),
    path('direccion/', views.CartAddressView.as_view(), name='cart-address'),
    path('resumen/', views.CartResumeView.as_view(), name='cart-resume'),
    path('delete/<int:cart_product>/', views.cart_product_delete_view, name='delete'),
    path('api/', include(router.urls)),
]
