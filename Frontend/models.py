from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class registrationdb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    Image = models.ImageField(upload_to="Images",null=True,blank=True)




class Leave_Request(models.Model):
    date = models.DateField()
    username = models.CharField(max_length=50, null=True, blank=True)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending')





