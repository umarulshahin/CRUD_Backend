from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializer import RegisterSerializer,UserSerializer,ImageUploadSerializer
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


@api_view(['GET'])  
@permission_classes([IsAuthenticated])  
def Dashboard(request):
    if request.method == 'GET':
        user = request.user
        
        data=CustomUser.objects.filter(email=user)
        serializer=UserSerializer(data,many=True)
           
        return Response(serializer.data)

    return Response({'error': "Method not allowed"})
   

@api_view(['POST'])
def Sign_Up(request):
    
   if request.method == 'POST':
       nested_data = request.data.get('data', {})
       serializer=RegisterSerializer(data=nested_data)  
      
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)  
       return Response({"error":serializer.errors})
    
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])    
def Image_Upload(request):
    
    if request.method == "PATCH":
        image = request.FILES.get('image')
        user_email = request.user.email
        print(image, "image")
        if not image:
            return Response({"error": "Image file is required"}, status=400)
        data = {"image": image, "user": user_email}

        serializer = ImageUploadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Image uploaded successfully"}, status=200)
        return Response({"error": serializer.errors}, status=400)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token["role"]=user.is_superuser
        
        return token

class MyTokenobtainedPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer
    
class Update_User(APIView):
    
    permission_classes([IsAuthenticated])
    def patch(self,request):
        
        id=request.data.get("id")
        
        obj=CustomUser.objects.filter(id=id).first()
        if not obj:
            return Response({"error": "User not found"})
        
        serializer=UserSerializer(obj,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error":serializer.errors})
    
    