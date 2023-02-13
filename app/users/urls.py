from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views._login, name='login'),
    path('logout/', views._logout, name='logout'),
    path('register/', views.register, name='register'),

    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile-edit/', views.edit_profile, name='profile-edit'),
    path('accounts/', views.accounts, name='accounts'),
    path('inbox/', views.inbox, name='inbox'),
    # path('read-inbox/<int:pk>/', views.read_inbox, name='read-inbox'),
    path('create-message/<int:pk>/', views.create_message, name='create-message'),
]
