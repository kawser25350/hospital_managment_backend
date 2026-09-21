from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='patient')
    image=models.ImageField(upload_to='patient/images')
    phone=PhoneNumberField(unique=True,blank=True,null=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.user.last_name} - {self.phone}"