from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=130)
    phone=PhoneNumberField(null=True,unique=True,blank=True)
    problem=models.TextField()