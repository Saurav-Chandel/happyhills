from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/',Signup, name='signup'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout')
]