from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PatientSerializer,RegistrationSerializer,LoginSerializer
from .models import Patient
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token

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

            token = default_token_generator.make_token(account)
            uid = urlsafe_base64_encode(force_bytes(account.pk))
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"

            email_body = render_to_string(
                "confirmation_email.html",
                {
                    "confirm_link": confirm_link,
                    "first_name": account.first_name,
                },
            )
            email = EmailMultiAlternatives(
                "Confirm Your Email.",
                "",
                to=[account.email],
            )
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response({"message":"Registraion Done.Please Check Your Email."},status=201)
        return Response(serializer.errors,status=400)

class LoginApiView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']

            user=authenticate(username=username,password=password)
            if user:
                token,_=Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token':token.key,'user_id':user.id})
            else:
                return Response({'error':"Invalid Credential"})
        return Response(serializer.errors)

class LogoutApiView(APIView):

    def get(self,request):
        Token.objects.filter(user=request.user).delete()
        logout(request)
        return redirect('login')

        
def active_account(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64)
        user=User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None
    if user and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect('login')
    else:
        return redirect('register')