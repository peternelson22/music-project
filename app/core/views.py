from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Album, Event, Song
from .forms import AlbumForm, SongForm
from .utils import paginate_albums



def album_store(request):
    albums = Album.objects.all()

    custom_range, albums = paginate_albums(request, albums, 6)

    context = {'albums': albums, 'custom_range': custom_range}
    return render(request, 'core/albums-store.html', context)


@login_required(login_url='login')
def songs(request, pk):
    album = Album.objects.get(id=pk)
    form = SongForm()

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.album = album
            song.save()
            return redirect('song', pk=album.id)

    context = {'album': album, 'form': form}
    return render(request, 'core/songs.html', context)


@login_required(login_url='login')
def add_album(request):
    profile = request.user.profile
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = profile
            album.save()
            return redirect('index')
    return render(request, 'core/album-form.html', {'form': form})


def event(request):
    events = Event.objects.all()

    context = {'events': events}
    return render(request, 'core/event.html', context)
