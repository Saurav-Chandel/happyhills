from django.db import models
from accounts.constant import *
# Create your models here.

class Banner(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(upload_to ='landing/',null=True,blank=True)
    is_active=models.BooleanField(default=False,blank=True,null=True)
    description=models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Images(models.Model):
    image=models.ImageField(upload_to='pictures',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class State(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(upload_to ='state/',null=True,blank=True)
    is_active=models.BooleanField(default=False,blank=True,null=True)
    description=models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Districts(models.Model):
    state=models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField(upload_to ='district/',null=True,blank=True)
    title=models.CharField(max_length=255,null=True,blank=True)
    is_active=models.BooleanField(default=False,blank=True,null=True)
    description=models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Iternary(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    days=models.CharField(max_length=255,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)

class Treks(models.Model):
    district=models.ForeignKey(Districts,on_delete=models.CASCADE,null=True,blank=True)
    t_image=models.ManyToManyField(Images)
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    route=models.TextField(null=True,blank=True)
    altitude=models.CharField(max_length=255,null=True,blank=True)
    trek_length=models.CharField(max_length=255,null=True,blank=True)
    duration=models.CharField(max_length=255,null=True,blank=True)
    difficulty_level=models.PositiveIntegerField(choices=difficulty_level,null=True,blank=True)
    best_season = models.CharField(max_length=255, blank=True, null=True)
    Iternary=models.ManyToManyField(Iternary)
    quick_facts = models.TextField(null=True,blank=True)
    guidance = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Events(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)   
    image=models.ImageField(upload_to ='events/',null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)