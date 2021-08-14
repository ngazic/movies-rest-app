from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django import views
from movies.models import Movie,StreamPlatform, Review
from .serializers import AdminSerializer, AccountSerializer
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from user_app.models import User


"""
======================================
User

"""

filter = {'is_staff':False, 'is_superuser':False}

class AccountListGV(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = User.get_users()
    serializer_class = AccountSerializer 
    
class AccountDetailsGV(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = User.get_users()
    serializer_class = AccountSerializer 

    
"""
======================================
Admin

"""

class AdminAccountListGV(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = User.get_admin_users()
    serializer_class = AdminSerializer 
    
class AdminAccountDetailsGV(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = User.get_admin_users()
    serializer_class = AdminSerializer 





