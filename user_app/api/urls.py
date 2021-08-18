from django import views
from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # users
    path('', views.AccountListGV.as_view(), name='account-list'),
    path('<int:pk>/', views.AccountDetailsGV.as_view(), name='account-list'),
    # administrators
    path('admin/', views.AdminAccountListGV.as_view(), name='account-list'),
    path('admin/<int:pk>/', views.AdminAccountDetailsGV.as_view(), name='account-list'),
    # JWT TOKEN ROUTES
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password/request/', views.RequestPasswordResetEmail.as_view(), name='password_reset_request'),
    path('password/request/<uidb64>/<token>/', views.PasswordTokenValidationAPI.as_view(), name='password_reset_confirm'),
    path('password/reset/', views.SetNewPasswordAPIView.as_view(), name='password_reset_request'),
]
