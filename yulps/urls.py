
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# Views
from products import views


urlpatterns = [
    path('', views.redirect_home_view),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('products/', include('products.urls', namespace='products')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
