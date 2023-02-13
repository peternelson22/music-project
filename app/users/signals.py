import email
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from app.settings import EMAIL_HOST_USER
from .models import Profile


def profile_create(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(user=user, first_name=user.first_name,
                                         last_name=user.last_name, email=user.email)

        subject = 'Welcome to One music'
        message = 'You will never need to leave here'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


def update_user(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.email = profile.email
        user.save()


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(profile_create, sender=User)
post_save.connect(update_user, sender=Profile)
post_delete.connect(delete_user, sender=Profile)
