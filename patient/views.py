from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PatientSerializer,RegistrationSerializer
from .models import Patient
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class PatientViewset(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer

class RegistratoinApiView(APIView):
    serializer_class=RegistrationSerializer
    
    
    def post(self,request):
        
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            account=serializer.save()
            return Response({"message":"Registraion Done"},status=201)
        return Response(serializer.errors,status=400)