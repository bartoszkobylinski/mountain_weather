from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import RegisterUserView

urlpatterns = [
    path('register_user/',RegisterUserView.as_view(template_name='register.html')),
    path('login/', auth_views.LoginView.as_view())
]