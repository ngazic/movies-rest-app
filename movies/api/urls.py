from django import views
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', views.MoviesListGV.as_view(), name='movie-list'),
    path('<int:pk>/', views.MovieDetailGV.as_view(), name='movie-detail'),
    path('', include(router.urls)),
    path('<int:pk>/review/', views.ReviewListGV.as_view(), name='review-list'),
    path('review/<int:pk>', views.ReviewDetailGV.as_view(), name='review-detail'),
    path('<int:pk>/review-create/', views.ReviewCreateGV.as_view(), name='review-create'),
]
