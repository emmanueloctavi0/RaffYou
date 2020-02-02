
# Django
from django.urls import path

# Views
from users import views


app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginViewCustom.as_view(), name='login'),
]