from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import RegisterUserView, CreatePost, PostDetailView, UserProfileView

urlpatterns = [
    path('register_user/', RegisterUserView.as_view(template_name='register.html'),name='register'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', UserProfileView.as_view(), name='profile'),
    path('accounts/profile/posts/', UserProfileView.as_view(),name='posts-list'),
    path('accounts/profile/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('accounts/profiel/posts/new',CreatePost.as_view(), name='create-post'),
]