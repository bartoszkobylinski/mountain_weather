from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='icon-user.png', upload_to='profile_picture')

    def __str__(self):
        return f"{self.user.username} profile"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='place_picture', blank=True)

    def __str__(self):
        return f" Post published {self.date} by {self.user.username}"
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk })