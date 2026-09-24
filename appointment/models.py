from django.db import models
from patient.models import Patient
from doctor.models import Doctor,AvailableTime

# Create your models here.

Appointment_type =[
    ("Online","Online"),
    ("Offline","Offline")
]

Appointment_status = [
    ("Running","Running"),
    ("Pending","Pending")
]






class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    avaliable_time=models.OneToOneField(AvailableTime,on_delete=models.CASCADE)
    appointment_status=models.CharField(choices=Appointment_status,max_length=12)
    appointment_types=models.CharField(choices=Appointment_type,max_length=12)
    symptom=models.TextField()
    cancel=models.BooleanField(default=False)
    appointment_date=models.DateTimeField(auto_now_add=True,blank=True,null=True)

