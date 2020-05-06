
# Django
from django.urls import include, path

# Django REST Framework
from rest_framework import routers

# Views
from carts.views import CartProductViewSet

router = routers.DefaultRouter()
router.register('', CartProductViewSet)

app_name = 'carts'


urlpatterns = [
    path('', include(router.urls)),
]
