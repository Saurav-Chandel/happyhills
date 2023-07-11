from django.shortcuts import render,redirect
from django.db.models import Q
from users.models import *
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.views.generic import View,TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

class AdminLoginView(TemplateView):
    def get(self, request, *args, **kwargs):
        return redirect('accounts:login')


def Login(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            return redirect('admin:index')
        return render(request, "registration/login.html")

    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate(username=email,password=password)
        if user is not None:
           login(request, user)
           messages.add_message(request, messages.INFO, 'Login Successfully.')
           return redirect('admin:index')
        else:
            messages.add_message(request, messages.INFO, 'Invalid Credentials')
            return render(request, "registration/login.html")

def Signup(request):
    if request.method=="GET":
        return render(request, "registration/signup.html")   

    if request.method == "POST":
        user=User.objects.create(first_name=request.POST.get('name'),
                            email=request.POST.get('email'),
                            username=request.POST.get('email')) 
        user.password=make_password(request.POST.get('password')) 
        user.save() 
        messages.add_message(request, messages.INFO, 'Signup Successfully.')
        return redirect('user:login')


@login_required
def Logout(request):
    logout(request)
    return redirect('user:login')