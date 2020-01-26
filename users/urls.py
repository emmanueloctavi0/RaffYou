
# Django
from django.urls import path

# Views
from users import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]