from django.db import models
from datetime import datetime


# Create your models here.
class Login(models.Model):
  ownername=models.CharField(max_length=100)
  email=models.EmailField(default='default@example.com')  
  password=models.CharField(max_length=50) 
  confirmpassword=models.CharField(max_length=50)
def __str__(self) :
  return self.ownername  
class Appointment(models.Model):
  doctorname=models.CharField(max_length=20)
  nameofowner=models.CharField(max_length=50)
  emailid=models.EmailField(default='default@example.com')
  contactno=models.IntegerField()
  location=models.CharField(max_length=50)
  petbreed=models.CharField(max_length=20)
  gender=models.CharField(max_length=7)
  age=models.IntegerField()
  description=models.CharField(max_length=100)
  
def __str__(self):
  return self.doctorname





