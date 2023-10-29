from django.db import models
import datetime

# Create your models here.
class registerdb(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    C_password=models.CharField(max_length=100,null=True,blank=True)

class empdb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Designation = models.CharField(max_length=50,null=True,blank=True)
    Date =  models.DateField(default=datetime.date.today)