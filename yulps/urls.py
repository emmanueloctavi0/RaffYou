
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# Views
from products import views


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('usuarios/', include('users.urls', namespace='users')),
    path('comida/', include('products.urls', namespace='products')),
    # API
    path('carrito/', include('carts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
