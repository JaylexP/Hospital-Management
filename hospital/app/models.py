from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Doctor(models.Model):
    Name= models.CharField(max_length=50)
    Mobile= models.IntegerField()
    special= models.CharField(max_length=50)
    email= models.CharField(max_length=50)

class Patient(models.Model):
    name= models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    mobile=models.IntegerField()
    address=models.TextField()


class Appoinment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    

    

 