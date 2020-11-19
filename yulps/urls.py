
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# Views
from core import views as core_views


def error_debug(request):
    return

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('usuarios/', include('users.urls', namespace='users')),
    path('comida/', include('products.urls', namespace='products')),
    path('pedidos/', include('orders.urls', namespace='orders')),
    # API
    path('carrito/', include('carts.urls')),
    path('api/', include('api.urls')),

    # Debugs
    path('404/', core_views.PageNotFoundView.as_view()),
    path('500/', error_debug),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = core_views.PageNotFoundView.as_view()
handler500 = core_views.server_error


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
