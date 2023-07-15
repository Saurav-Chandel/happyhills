from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'loggers'

urlpatterns = [
    path('logs/', Logger, name='logs'),
]