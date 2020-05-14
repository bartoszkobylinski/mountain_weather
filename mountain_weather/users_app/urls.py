from django.urls import path, include
from .views import RegisterUserView

urlpatterns = [
    path('register_user/',RegisterUserView.as_view(template_name='register.html')),
]