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
    states,districts,treks=[],[],[]
    state=State.objects.all().order_by('-created_at')
    for s in state:
        states.append(s)
        districts.append([[i,Treks.objects.filter(district_id=i.id)] for i in s.districts_set.all()])
    lst=list(zip(states,districts))
    return render(request,'frontend/index.html',{
        'banners':banners,
        'state':state,
        'lst':lst
    })

def TrekDetail(request,id):
    return render(request,'frontend/trek-details.html',{
    })    


def BannerImages(request):
    banners=Banner.objects.all().order_by('-id')
    return render(request,'admin/banner/banner_list.html',{
        'banners':banners,
        'head_title':'Banners'
    })

def AddBannerImages(request):
    if request.method == 'POST':
        Banner.objects.create(
            title=request.POST.get('title'),
            image=request.FILES.get('image'),
            description=request.POST.get('description')
        )
        messages.add_message(request, messages.INFO, 'Banner Added Successfully!')
        return redirect('frontend:banner')
    return render(request,'admin/banner/add_banner.html',{'head_title':'Banners'})    

def DeleteBanner(request,id):
    Banner.objects.get(id=id).delete()
    return redirect('frontend:banner')

def ViewBanners(request,id):
    banner=Banner.objects.get(id=id)
    return render(request,'admin/banner/view_banner.html',{'head_title':'Banners'})    


def EditBanner(request,id):
    banner=Banner.objects.get(id=id)
    return render(request,'admin/banner/edit_banner.html',{'head_title':'Banners'})

def StateList(request):
    state=State.objects.all().order_by('-created_at')
    return render(request,'admin/state/state_list.html',{
        'head_title':'States',
        'state':state
        })


def AddState(request):
    if request.method=="GET":
        return render(request,'admin/state/add_state.html',{'head_title':'States'})

    if request.method=="POST":
        State.objects.create(
            title=request.POST.get('title'),
            image=request.FILES.get('image'),
            description=request.POST.get('description'),
        )
        messages.add_message(request, messages.INFO, 'State Added Successfully!')
        return redirect('frontend:state_list')

def EditState(request,id):
    return render(request,'admin/state/add_state.html',{'head_title':'States'})    

def ViewState(request,id):
    return render(request,'admin/state/view_state.html',{'head_title':'States'})        

def DeleteState(request,id):
    State.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'State Deleted Successfully!')
    return redirect('frontend:state_list')     

def DistrictList(request):
    districts=Districts.objects.all().order_by('-created_at')
    return render(request,'admin/district/district_list.html',{
        'head_title':'Districts',
        'districts':districts
    })

def AddDistrict(request):
    if request.method == "GET":
        states=State.objects.all().order_by('-created_at')
        return render(request,'admin/district/add_district.html',{
            'head_title':'Districts',
            'states':states
        })
    if request.method == 'POST':
        Districts.objects.create(
            title=request.POST.get('title'),
            state_id=request.POST.get('state'),
            image=request.FILES.get('image'),
            description=request.POST.get('description'),
            )
        messages.add_message(request, messages.INFO, 'District Added Successfully!')
        return redirect('frontend:district_list')    

def ViewDistrict(request):
    return render(request,'admin/district/view_district.html',{'head_title':'Districts'})    

def EditDistrict(request,id):
    return render(request,'admin/district/edit_district.html',{'head_title':'Districts'})    

def DeleteDistrict(request,id):
    Districts.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'District Deleted Successfully!')
    return redirect('frontend:district_list') 

def TrekList(request):
    treks=Treks.objects.all().order_by('-created_at')
    return render(request,'admin/trek/trek_list.html',{
        'head_title':'Treks',
        'treks':treks
    })

def AddTrek(request):
    if request.method == 'GET':
        districts=Districts.objects.all().order_by('created_at')
        return render(request,'admin/trek/add_trek.html',{
            'head_title':'Treks',
            'districts':districts
        })
    if request.method == 'POST':
        trek=Treks.objects.create(
            title=request.POST.get('title'),
            district_id=request.POST.get('district'),
            # image=request.FILES.get('image'),
            description=request.POST.get('description'),
        )
        for i in request.FILES.getlist('image'):
            trek.t_image.add(Images.objects.create(image=i))
        trek.save()    
        messages.add_message(request, messages.INFO, 'Trek Added Successfully!')
        return redirect('frontend:trek_list')    

def ViewTrek(request):
    return render(request,'admin/trek/view_trek.html',{'head_title':'Treks'})    

def EditTrek(request,id):
    return render(request,'admin/trek/edit_trek.html',{'head_title':'Treks'})    

def DeleteTrek(request,id):
    Treks.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'Trek Deleted Successfully!')
    return redirect('frontend:trek_list')    