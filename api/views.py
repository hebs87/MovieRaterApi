from django.contrib.auth.models import User
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
        A function that allows the user to rate a movie - if a record already exists,
        the existing rating will be updated. If not, a new record will be created
        """
        if 'stars' in request.data:
            # We display this message if there are stars in request to rate the movie
            # and we print the movie title if the request is successful
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            # user = request.user
            # As we currently don't have authentication, we can just specify a dummy user ID
            user = User.objects.get(id=1)

            # If we have something in the database for the user and movie combo already, we
            # will update the existing record. If not, then we will create a new record
            try:
                # We get the relevant rating record based on the user ID and movie ID
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                # Update the stars rating with the new rating
                rating.stars = stars
                rating.save()
                # We serialize the rating data, specify that it is only one record (many=False)
                serializer = RatingSerializer(rating, many=False)
                # We display an object with the success message and the serialized data
                response = {
                    'message': 'Rating updated',
                    'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            except:
                # We create a new record and pass in the user, movie and stars values
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                # We serialize the rating data, specify that it is only one record (many=False)
                serializer = RatingSerializer(rating, many=False)
                # We display an object with the success message and the serialized data
                response = {
                    'message': 'Rating created',
                    'result': serializer.data
                }
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
