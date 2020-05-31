
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
    DetailView
    )
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import CreatePostForm
from .models import Post

from zakopane_weather.views import IndexView

from .forms import CreateUserForm

class RegisterUserView(FormView):
    template_name = 'register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Account created for {username}')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super(RegisterUserView, self).form_valid(form)
    
class CreatePost(CreateView):
    model = Post
    fields = [ 'title', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    queryset= Post.objects.all()
    template_name = 'accounts/profile.html'
    

class PostDetailView(DetailView):
    model = Post
    
class UpdatePost(UpdateView):
    pass
