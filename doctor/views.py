from django.shortcuts import render
from rest_framework import viewsets
from .models import Designation,Doctor,Specialization,AvailableTime
from .serializers import DesignationSerializer,DoctorSerializer,SpecializationSerializer,AvailableTimeSerializer
# Create your views here.

class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    queryset=Designation.objects.all()
    serializer_class=DesignationSerializer

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset=Specialization.objects.all()
    serializer_class=SpecializationSerializer

class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset=AvailableTime.objects.all()
    serializer_class=AvailableTimeSerializer