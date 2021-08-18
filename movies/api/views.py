from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django import views
from movies.models import Movie,StreamPlatform, Review
from .serializers import MovieSerializer, PlatformSerializer, ReviewSerializer
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from .permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly

# Create your views here.
# AV suffix stands for API VIEW
# GV suffix stands for GENERIC VIEW (this is common GET, PUT, DELETE, POST implementations of API VIEW)
# VS suffix stands for View Set


    
"""
======================================
Review 

"""

class ReviewListGV(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(movie=pk)


class ReviewDetailGV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permissions = [permissions.IsAuthenticated]
    


class ReviewCreateGV(generics.CreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        movie = Movie.objects.get(pk=pk)
        print(self.request.user)
        serializer.save(movie=movie)
    
"""
======================================
Stream Platform

"""
    
class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = PlatformSerializer


class StreamPlatformListGV(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = PlatformSerializer
    


"""
======================================
Movies

"""

class MoviesListGV(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailGV(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrReadOnly,IsAdminOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    
# class MoviesListAV(APIView):

#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

            
# class MovieDetailAV(APIView):

#     def get(self, request, pk):
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Not found'}, status= status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


