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

@login_required
def UserList(request):
    return render(request,'users/users.html')