from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = bio = models.TextField(blank=True, null=True)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile, created = Profile.objects.get_or_create(user=instance)
        else:
            for user in User.objects.all():
                Profile.objects.get_or_create(user=user)
    post_save.connect(create_user_profile, sender=User)


    def __str__(self):
        return f'{self.user.username} Profile'
