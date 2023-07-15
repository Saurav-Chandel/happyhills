from django.db import models

# Create your models here.


class Banner(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(upload_to ='landing/',null=True,blank=True)
    description=models.TextField(null=True,blank=True)

