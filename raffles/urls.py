
# Django
from django.urls import path

# Views
from raffles import views


app_name = 'raffles'

urlpatterns = [
    path('', views.RaffleHomeView.as_view(), name='home'),
]
