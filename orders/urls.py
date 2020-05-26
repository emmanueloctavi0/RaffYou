
# Django
from django.urls import path

# Views
from orders import views

app_name = 'orders'


urlpatterns = [
    path('', views.OrderListView.as_view(), name='order-list'),
]
