from django.shortcuts import render
from MainApp.models import *
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status





# Create your views here.

@api_view(['GET'])  
@permission_classes([IsAuthenticated])  
def Admin_Dashboard(request):
    if request.method == 'GET':
        user = request.user
        
        data=CustomUser.objects.exclude(is_superuser=True)
        serializer=UserSerializer(data,many=True)
           
        return Response(serializer.data)

    return Response({'error': "Method not allowed"})


class UserDelete(APIView):
    
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        try:
            user_id = request.data.get("id")
            print(request.data.get("id"))
            if not user_id:
                return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            user = CustomUser.objects.filter(id=user_id).first()
            if not user:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            
            user.delete()
            return Response({"success": "Deleted successfully"}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": f"Something went wrong: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

   
