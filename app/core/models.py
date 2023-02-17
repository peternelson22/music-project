from django.db import models
from PIL import Image
from users.models import Profile


class Album(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    album_title = models.CharField(max_length=200)
    logo = models.ImageField(null=True, blank=True, default='blankimage.png', upload_to='images/albums')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'album'
        ordering = ['-pub_date']

    def __str__(self) -> str:
        return self.album_title


    @property
    def imageURL(self):
        try:
            url = self.logo.url
        except:
            url = ''
        return url

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    mp3 = models.FileField()

    class Meta:
        db_table = 'song'

    def __str__(self):
        if self.song_title is not None:
            return self.song_title
        return


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    flyer = models.ImageField(upload_to='images/events', default='blankimage.png', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'event'

    def __str__(self) -> str:
        return self.title
