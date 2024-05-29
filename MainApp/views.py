from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializer import RegisterSerializer,UserSeializer
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.


@api_view(['GET'])  
@permission_classes([IsAuthenticated])  
def Dashboard(request):
    if request.method == 'GET':
        user = request.user
        data=CustomUser.objects.filter(email=user)
        serializer=UserSeializer(data,many=True)
           
        return Response(serializer.data)

    return Response({'error': "Method not allowed"})
   

@api_view(['POST'])
def Sign_Up(request):
    
   if request.method == 'POST':
       nested_data = request.data.get('data', {})
       serializer=RegisterSerializer(data=nested_data)  
      
       if serializer.is_valid():
           serializer.save()
           return Response({"Success":"User created"})  
       return Response({"error":serializer.errors})
    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...
        
        return token

class MyTokenobtainedPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer
    
 