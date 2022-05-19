from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MoviesSerializer
from .models import Movies
#provided by django rest framework to handle GET and POST requests for us
class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all().order_by('title')
    serializer_class = MoviesSerializer