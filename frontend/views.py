from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.

# @login_required
def index(request):
    active_banners=Banner.objects.all().first()
    banners=Banner.objects.filter(is_active=True).order_by('-id')
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

def StateDetail(request,id):
    states,districts,treks=[],[],[]
    state=State.objects.all().order_by('-created_at')
    for s in state:
        states.append(s)
        districts.append([[i,Treks.objects.filter(district_id=i.id)] for i in s.districts_set.all()])
    lst=list(zip(states,districts))
    state=State.objects.get(id=id)
    return render(request,'frontend/trek-details.html',{
        'lst':lst,
        'state':state
    })  

def DistrictDetail(request,id):
    states,districts,treks=[],[],[]
    state=State.objects.all().order_by('-created_at')
    for s in state:
        states.append(s)
        districts.append([[i,Treks.objects.filter(district_id=i.id)] for i in s.districts_set.all()])
    lst=list(zip(states,districts))
    district=Districts.objects.get(id=id)
    return render(request,'frontend/trek-details.html',{
        'lst':lst,
        'district':district
    })  


def TrekDetail(request,id):
    states,districts,treks=[],[],[]
    state=State.objects.all().order_by('-created_at')
    for s in state:
        states.append(s)
        districts.append([[i,Treks.objects.filter(district_id=i.id)] for i in s.districts_set.all()])
    lst=list(zip(states,districts))
    trek=Treks.objects.get(id=id)
    return render(request,'frontend/trek-details.html',{
        'lst':lst,
        'trek':trek
    })    

def BannerImages(request):
    banners=Banner.objects.all().order_by('-id')
    if request.GET.get('title'):
        banners=banners.filter(title__icontains=request.GET.get('title'))
    if request.GET.get('description'):
        banners=banners.filter(description__icontains=request.GET.get('description'))    
    if request.GET.get('status'):
        banners=banners.filter(is_active=request.GET.get('status'))       
    if request.GET.get('created_on'):
        banners=banners.filter(created_at__date=request.GET.get('created_on'))     
    if request.GET and not banners:
        messages.add_message(request, messages.INFO, 'No Data Found!')
    return render(request,'admin/banner/banner_list.html',{
        'banners':banners,
        'head_title':'Banners',
        'title':request.GET.get('title',''),
        'description':request.GET.get('description',''),
        'status':request.GET.get('status',''),
        'created_on':request.GET.get('created_on','')
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
    return render(request,'admin/banner/view_banner.html',{
        'head_title':'Banners',
        'banner':banner
        })    

def ActivatDeactivateBanner(request,id):
    banner=Banner.objects.get(id=id)
    if banner.is_active:
        banner.is_active=False
        # messages.add_message(request, messages.INFO, 'Banner DeActivated Successfully!')
    else:
        banner.is_active=True
        # messages.add_message(request, messages.INFO, 'Banner Activated Successfully!')
    banner.save()    
    return redirect('frontend:view_banner',id=id)

def EditBanner(request,id):
    banner=Banner.objects.get(id=id)
    if request.method == 'POST':
        if request.POST.get('title'):
            banner.title=request.POST.get('title')
        if request.FILES.get('image'):
            banner.image=request.FILES.get('image')
        if request.POST.get('description'):
            banner.description=request.POST.get('description')   
        banner.save()
        return redirect('frontend:banner')         
    return render(request,'admin/banner/edit_banner.html',{
        'head_title':'Banners',
        'banner':banner
        })

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
    state=State.objects.get(id=id)
    if request.method == 'POST':
        if request.POST.get('title'):
            state.title=request.POST.get('title')
        if request.FILES.get('image'):
            state.image=request.FILES.get('image')
        if request.POST.get('description'):
            state.description=request.POST.get('description')   
        state.save()
        return redirect('frontend:state_list')  
    return render(request,'admin/state/edit_state.html',{
        'head_title':'States',
        'state':state
        })    

def ViewState(request,id):
    state=State.objects.get(id=id)
    return render(request,'admin/state/view_state.html',{
        'head_title':'States',
        'state':state
        })        

def ActivatDeactivateState(request,id):
    state=State.objects.get(id=id)
    if state.is_active:
        state.is_active=False
        # messages.add_message(request, messages.INFO, 'Banner DeActivated Successfully!')
    else:
        state.is_active=True
        # messages.add_message(request, messages.INFO, 'Banner Activated Successfully!')
    state.save()    
    return redirect('frontend:view_state',id=id)
    
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
            route=request.POST.get('route'),
            altitude=request.POST.get('altitude'),
            trek_length=request.POST.get('trek_length'),
            duration=request.POST.get('duration'),
            difficulty_level=request.POST.get('level'),
            best_season=request.POST.get('best_season'),
        )
        for i in request.FILES.getlist('property_images'):
            trek.t_image.add(Images.objects.create(image=i))
        trek.save()    
        messages.add_message(request, messages.INFO, 'Trek Added Successfully!')
        return redirect('frontend:trek_list')    

def ViewTrek(request,id):
    trek=Treks.objects.get(id=id)
    return render(request,'admin/trek/view_trek.html',{
        'head_title':'Treks',
        'trek':trek

    })    

def EditTrek(request,id):
    if request.method == 'GET':
        trek=Treks.objects.get(id=id)
        districts=Districts.objects.all().order_by('created_at')
        return render(request,'admin/trek/edit_trek.html',{
            'head_title':'Treks',
            'trek':trek,
            'districts':districts
            }) 
    if request.method == 'POST':
        print(id,'22222222222222222')
        return redirect('frontend:edit_trek',id=id)        

def DeleteTrek(request,id):
    Treks.objects.get(id=id).delete()
    messages.add_message(request, messages.INFO, 'Trek Deleted Successfully!')
    return redirect('frontend:trek_list')    