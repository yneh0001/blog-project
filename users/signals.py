"""
This module is signal the profile everytime a new user created to create a new profile
"""

from django.db.models.signals import post_save #the signal is sent after new user is saved (created)
from django.contrib.auth.models import User #who is going to signal
from django.dispatch import receiver #reciver of the signal 
from .models import Profile #the profile which will be created


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()