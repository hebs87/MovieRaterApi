from rest_framework import viewsets
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    """
    A viewset to render the Movie model and serializer
    in an API format
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RatingViewSet(viewsets.ModelViewSet):
    """
    A viewset to render the Rating model and serializer
    in an API format
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
