from rest_framework import serializers
from .models import Movie, Rating


class MovieSerializer(serializers.ModelSerializer):
    """
    A serializer to serialize the data passed into the
    Movie model
    """
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description')


class RatingSerializer(serializers.ModelSerializer):
    """
    A serializer to serialize the data passed into the
    Rating model
    """
    class Meta:
        model = Rating
        fields = ('id', 'movie', 'user', 'stars')
