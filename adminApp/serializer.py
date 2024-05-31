from rest_framework import serializers
from MainApp.models import *


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=CustomUser
        fields=['username', 'email', 'phone', 'profile','id']
        read_only_fields = ['id']
        