from rest_framework import status, generics
from rest_framework.response import Response
from django import views
from movies.models import Movie,StreamPlatform, Review
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from user_app.models import User
from user_app.utils import Util
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import  urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from .serializers import (AdminSerializer, 
                          AccountSerializer, 
                          ResetPasswordEmailRequestSerializer,
                          SetNewPasswordSerializer,)


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


"""
======================================
Password change with email 

"""

class RequestPasswordResetEmail(generics.GenericAPIView):
    queryset = None
    serializer_class = ResetPasswordEmailRequestSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(get_current_site(request).domain)
        email = request.data.get('email', '')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = settings.RESET_PASSWORD_DOMAIN if settings.RESET_PASSWORD_DOMAIN else get_current_site(request).domain
            relative_link = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
            abs_url = 'http://' + current_site + relative_link
            email_body = 'Hi ' + user.username + '\n Use this link to reset your password : ' + abs_url
            email_data = {
                'subject': f'no-reply',
                'to': [email,],
                'body': email_body,
                }
            Util.send_email(**email_data)

        return Response({'success': f'Link for password reset was sent to {email}'})

        
class PasswordTokenValidationAPI(generics.GenericAPIView):

    def get(self, request, uidb64, token):
        
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'}, status.HTTP_400_BAD_REQUEST)
            
            return Response({'success': True, 'message': 'credentials valid', 'uidb64': uidb64, 'token': token})
        except:
            return Response({'error': 'Token and/or user ID are not valid, please request a new ones'}, status.HTTP_400_BAD_REQUEST)



class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)
