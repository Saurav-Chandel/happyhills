from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'frontend'

urlpatterns = [
    path('', index, name='index'),
    path('banners/', BannerImages, name='banner'),
    path('add-banner/', AddBannerImages, name='add_banner'),
]