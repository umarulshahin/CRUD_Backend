from django.shortcuts import render
from MainApp.models import *
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated



# Create your views here.

@api_view(['GET'])  
# @permission_classes([IsAuthenticated])  
def Admin_Dashboard(request):
    if request.method == 'GET':
        user = request.user
        
        data=CustomUser.objects.exclude(is_superuser=True)
        serializer=UserSerializer(data,many=True)
           
        return Response(serializer.data)

    return Response({'error': "Method not allowed"})
   
