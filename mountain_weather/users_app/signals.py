from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print(f'{instance.username} profile is created!')


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created is False:
        instance.profile.save()
        print(f'{instance.username} profile has been updated')
