from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(default="blankimage.png", upload_to="images/users")
    social_media = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True, related_name='messages')
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'message'
        ordering = ['-created']

    def __str__(self):
        return self.subject
