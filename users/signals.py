from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import MyProfile


@receiver(post_save, sender=User)
def create_myprofile(sender, instance, created, **kwargs):
    if created:
        MyProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_myprofile(sender, instance, **kwargs):
    instance.myprofile.save()
