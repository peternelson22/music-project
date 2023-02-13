from datetime import datetime
from random import random
from time import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserForm, MessageForm
from .models import Profile
from core.models import Album, Song
from .utils import paginate_profiles, paginate_msgs
from django.utils import timezone


def index(request):
    albums = Album.objects.all().order_by('-pub_date')

    latest_albums = albums
    songs = Song.objects.all().order_by('?')
    top_albums = Album.objects.filter(pub_date__lt=timezone.now())

    context = {'albums': albums[:5], 'latest_albums': latest_albums[:2],
               'top_albums': top_albums[3:6], 'songs': songs[:3]}
    return render(request, 'users/index.html', context)


def _login(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Bad credentials')
        else:
            login(request, user)
            return redirect('index')
    return render(request, 'users/login.html')


def _logout(request):
    logout(request)
    messages.info(request, 'User successfully logged out')
    return redirect('login')


def register(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            messages.success(request, 'Successfully registered')
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'something went wrong')

    return render(request, 'users/register.html', {'form': form})


def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    return render(request, 'users/profile.html', {'profile': profile})


@login_required(login_url='login')
def edit_profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(profile)

    return render(request, 'users/profile-form.html', {'form': form})


def accounts(request):
    profiles = Profile.objects.all()

    custom_range, profiles = paginate_profiles(request, profiles, 6)
    context = {'profiles': profiles, 'custom_range': custom_range}
    return render(request, 'users/accounts.html', context)


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile

    msgs = profile.messages.all()
    custom_range, msgs = paginate_msgs(request, msgs, 2)
    context = {'msgs': msgs, 'custom_range': custom_range}
    return render(request, 'users/inbox.html', context)


@login_required(login_url='login')
def create_message(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.first_name
                message.email = sender.email

            message.save()
            return redirect('index')

    return render(request, 'users/message_form.html', {'form': form})
