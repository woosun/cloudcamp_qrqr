from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from twitter.utils import rename_imagefile_to_uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField(null=True, upload_to=rename_imagefile_to_uuid, max_length=255, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return "User"
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()