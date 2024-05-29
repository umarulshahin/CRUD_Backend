from django.urls import path
from MainApp.views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path ('dashboard/',Dashboard,name="dashboard"),
    path('signup/',Sign_Up,name="signup"),
    path('token/',MyTokenobtainedPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    
    
]
