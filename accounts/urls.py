from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('user_login',user_login, name='user_login'),
    path('user_creation',user_creation, name='user_creation'),
    ]