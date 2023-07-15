from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.

# @login_required
def index(request):
    active_banners=Banner.objects.all().first()
    banners=Banner.objects.all().order_by('-id')
    return render(request,'frontend/index.html',{'banners':banners,'active_banner':active_banners})

def BannerImages(request):
    return render(request,'admin/banner/banner_list.html')


def AddBannerImages(request):
    if request.method == 'POST':
        Banner.objects.create(
            title=request.POST.get('title'),
            image=request.FILES.get('image'),
            description=request.POST.get('description')
        )
        messages.add_message(request, messages.INFO, 'Landing Picture Added Successfully!')
        return redirect('frontend:banner')
    return render(request,'admin/banner/add_banner.html')    


