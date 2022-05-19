'''   
loadedMovies.push({
          id: key,
          title: data[key].title,
          openingText: data[key].openingText,
          releaseDate: data[key].releaseDate,
        })
'''
from rest_framework import serializers
from .models import Movies

class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movies
        fields = ('id', 'title', 'openingText', 'releaseDate')