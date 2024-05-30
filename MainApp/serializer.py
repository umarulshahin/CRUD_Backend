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
        
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CustomUser
        fields=['username', 'email', 'phone', 'profile','id']
        read_only_fields = ['id']
        

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()
    user = serializers.EmailField()
    
    def create(self, validated_data):
        user = CustomUser.objects.filter(email=validated_data["user"]).first()
        if user:
            user.profile = validated_data["image"]
            user.save()
            return user
        raise serializers.ValidationError("User not found")
              
