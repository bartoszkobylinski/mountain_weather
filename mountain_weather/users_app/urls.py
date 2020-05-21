from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import RegisterUserView
from django.views.generic import TemplateView

urlpatterns = [
    path('register_user/',RegisterUserView.as_view(template_name='register.html')),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile')
]