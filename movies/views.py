# from django.shortcuts import render
# from django.http import JsonResponse
# from django import views
# from .models import Movie

# # Create your views here.

# class ListView(views.View):
#     def get(self, request, *args, **kwargs):
#         all_movies = Movie.objects.order_by('title').values()
#         data = {'movies': list(all_movies)}
#         return JsonResponse(data)

#     # def post(self, request, *args, **kwargs):
#     #     return json('POST request!')


# def singleView(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'title': movie.title,
#         'description': movie.description,
#         'active': movie.active,
#     }
#     return JsonResponse(data)
