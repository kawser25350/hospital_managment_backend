from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model=Patient
        fields='__all__'



class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm_password']
    def save(self):
        username=self.validated_data['username']
        email=self.validated_data['email']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        pass1=self.validated_data['password'] 
        pass2=self.validated_data['confirm_password']
        
        if pass1!=pass2:
            raise serializers.ValidationError({'error':"password dosen't match."}); 
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':"Email already Exits"}); 
        account = User(username=username,email=email,first_name=first_name,last_name=last_name)
        account.set_password(pass1)
        account.is_active = False
        account.save()
        print(account)
        return account

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
    