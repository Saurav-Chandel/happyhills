from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .constant import *
# from store.models import *
from django.conf import settings
# Create your models here.



class User(AbstractUser):
     role_id=models.PositiveIntegerField(choices=user_role,null=True,blank=True)
     phone=models.CharField(max_length=255,blank=True,null=True)
     email=models.EmailField(max_length=250,unique=True,blank=True,null=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
            return str(self.first_name)

