from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PatientSerializer
from .models import Patient

# Create your views here.


class PatientViewset(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
