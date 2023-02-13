
from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.admin_user, name='adminuser'),
]
