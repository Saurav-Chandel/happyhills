from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'users'

urlpatterns = [
    path('users-list/', UserList, name='users_list'),
]