
from django.contrib.auth import login, authenticate
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
from .models import Post
from .forms import CreateUserForm


class RegisterUserView(FormView):
    '''
    Registration template view
    '''
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
    '''
    Creating a Post template view
    '''
    model = Post
    fields = ['title', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class UserProfileView(ListView):
    '''
    Profile template view
    '''
    template_name = 'accounts/profile.html'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class PostDetailView(DetailView):
    '''
    Detailed template view for a posted picture by user
    '''
    model = Post


class UpdatePost(UpdateView):
    '''
    View for template updating a Post by user
    '''
    pass


class DeletePost(DeleteView):
    '''
    View for template deleting a Post by user
    '''
    pass
