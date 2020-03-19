from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
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

    # The decorator stipulates that we are allowing only the POST method on the function,
    # and the detail=True means that we can only call it on a specific movie (ID), so we
    # will need to provide the ID of the movie we want to call it on. False would mean it
    # applies to the whole list of movies
    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        """
        A function that allows the user to rate a movie
        """
        if 'stars' in request.data:
            # We display this message if there are stars in request to rate the movie
            # and we print the movie title if the request is successful
            movie = Movie.objects.get(id=pk)
            print('Movie title:', movie.title)

            response = {'message': 'It\'s working'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            # We display this message if the user hasn't provided a star rating
            response = {'message': 'You need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    """
    A viewset to render the Rating model and serializer
    in an API format
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
