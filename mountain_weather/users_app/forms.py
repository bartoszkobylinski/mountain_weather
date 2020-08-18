from django.forms import TextInput, EmailInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post


class CreateUserForm(UserCreationForm):
    '''
    Registration Form for user
    '''

    password1 = forms.CharField(
        max_length=16, label='password', widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': '********'}
                               ))
    password2 = forms.CharField(
        max_length=16, label="repeat password", widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': '********'}
            )
            )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        widgets = {
            'username': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'username'
                    }
                ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'your@email.com'}
                ),
                }


class CreatePostForm(forms.ModelForm):
    '''
    Form for uploading a picture
    '''
    class Meta:
        model = Post
        fields = [
            'title',
            'image'
        ]


class DeletePostForm(forms.ModelForm):
    """
    Form for removing a picture
    """
    class Meta:
        model = Post
        fields = [
            'title',
        ]
