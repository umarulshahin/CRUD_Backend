from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.Serializer):
    
    username=serializers.CharField()
    lastname=serializers.CharField()
    email=serializers.EmailField()
    phone=serializers.CharField()
    password=serializers.CharField()
    
    def validate(self,data):
        if data["email"]:
            if CustomUser.objects.filter(email=data["email"]).exists():
                raise serializers.ValidationError("Email alredy exist")
            if CustomUser.objects.filter(phone=data["phone"]).exists():
                raise serializers.ValidationError("Phone number already exist")
            return data
        
    def create(self,validate_data):
        user=CustomUser.objects.create_user(
               username=validate_data["username"],
               last_name=validate_data["lastname"],
               email=validate_data["email"],
               phone=validate_data["phone"],
               password=validate_data["password"]    
        )
        user.save()

        return validate_data
        
        
class UserSeializer(serializers.ModelSerializer):
    
    class Meta:
        model=CustomUser
        fields=['username', 'email', 'phone', 'profile']