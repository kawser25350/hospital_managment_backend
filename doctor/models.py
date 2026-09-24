from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from autoslug import AutoSlugField
from patient.models import Patient


star_choices=[
    (1,'⭐'),
    (2,'⭐⭐'),
    (3,'⭐⭐⭐'),
    (4,'⭐⭐⭐⭐'),
    (5,'⭐⭐⭐⭐⭐'),

]

class Specialization(models.Model):
    name=models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)   

    def __str__(self): 
        return f"{self.name} - {self.slug}"


class Designation(models.Model):
    name=models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True) 

    def __str__(self): 
        return f"{self.name} - {self.slug}"

class AvailableTime(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


# Create your models here.
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='doctor')
    designation=models.ManyToManyField(Designation)
    specialization=models.ManyToManyField(Specialization)
    available_time=models.ManyToManyField(AvailableTime) 
    image=models.ImageField(upload_to='doctor/images')
    phone=PhoneNumberField(unique=True,blank=True,null=True)
    fee=models.IntegerField(default=0)
    meetlink=models.CharField(null=True,blank=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.user.last_name} - {self.phone}"

class Review(models.Model):
    reviewer=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE);
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    rating =models.PositiveIntegerField(choices=star_choices)

