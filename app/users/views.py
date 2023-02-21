from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, MessageForm
from .models import Profile, User
from core.models import Album, Song
from .utils import paginate_profiles, paginate_msgs
from django.utils import timezone


def index(request):
    albums = Album.objects.order_by('-pub_date').distinct()
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
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
        except:
            pass

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Bad credentials')
    return render(request, 'users/login.html')


def _logout(request):
    logout(request)
    messages.info(request, 'User successfully logged out')
    return redirect('login')


def register(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken... pls try another one')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Name already taken... pls try another one')
                return redirect('register')
            else:
                user = User.objects.create_user(name=name, email=email, username=username, password=password)
                user.save()
                
                messages.success(request, 'Successfully registered...')
                user_login = auth.authenticate(email=email, password=password)
                auth.login(request, user_login)
                return redirect('index')
        else:
            messages.error(request, 'Password not matching...')
            return redirect('register')
    
    return render(request, 'users/register.html')



def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    album_count = Album.objects.filter(owner=profile).count()
    return render(request, 'users/profile.html', {'profile': profile, 'album_count': album_count})


@login_required(login_url='login')
def edit_profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=profile.id)

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
                message.name = sender.name
                message.email = sender.email

            message.save()
            return redirect('index')

    return render(request, 'users/message_form.html', {'form': form})
