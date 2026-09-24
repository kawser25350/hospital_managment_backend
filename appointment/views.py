from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

# Create your views here.
class AppointmentViewset(viewsets.ModelViewSet):
    queryset=Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    def get_queryset(self):
        queryset=super().get_queryset()

        patient_id=self.request.query_params.get('patient')
        doctor_id=self.request.query_params.get('doctor')
        date_id=self.request.query_params.get('date')

        if patient_id:
            queryset=queryset.filter(patient_id=patient_id)
        if doctor_id:
            queryset=queryset.filter(doctor_id=doctor_id)
        if date_id:
            queryset=queryset.filter(appointment_date=date_id)
        return queryset