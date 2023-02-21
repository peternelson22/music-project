from django import forms
from .models import Album, Song


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_title', 'logo']

        widgets = {
            'album_title': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['song_title', 'description', 'mp3']

        widgets = {
            'song_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'mp3': forms.FileInput(attrs={'class': 'form-control'}),
        }
