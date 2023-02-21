from django.urls import path
from . import views


urlpatterns = [
    path('albums-store/', views.album_store, name='albums-store'),
    path('song/<int:pk>/', views.songs, name='song'),
    path('album/', views.add_album, name='album'),

    path('event/', views.event, name='event'),

]
