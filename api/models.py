from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


# Create your models here.
class Movie(models.Model):
    """
    A model to hold the movie details
    """
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def no_of_ratings(self):
        """
        A function that calculates the total number of ratings for the movie
        """
        # Filter the movie in the Rating model that matches the queried movie
        ratings = Rating.objects.filter(movie=self)
        # Return the length of the array, which give us the number of ratings
        return len(ratings)

    def avg_rating(self):
        """
        A function that calculates the average rating of a particular movie
        """
        ratings = Rating.objects.filter(movie=self)
        # We set the sum to 0, loop over the ratings and add the stars to the sum
        sum = 0

        for rating in ratings:
            sum += rating.stars

        # If there are ratings, then we calculate the int average. If not, we return 0
        if len(ratings) > 0:
            avg = int(sum / len(ratings))
        else:
            avg = 0

        return avg

    def __str__(self):
        return self.title


class Rating(models.Model):
    """
    A model to hold the rating for specific movies
    It is linked to the Movie model using the Foreign Key
    The on_delete property ensures that the rating and the
    user are removed if a particular Movie or User model
    is deleted
    """
    # The movie that the rating is for
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # The user who created the rating (allows us to have only one
    # rating per user per movie
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # We use the Min and Max value validators to ensure that the value can only be between 1 and 5
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        # Ensures that we can't create a duplicate record for the same user and movie combo
        unique_together = (('user', 'movie'),)
        # Indexes the user and movie values together
        index_together = (('user', 'movie'),)

    def __str__(self):
        return '{} gave {} a {} star rating'.format(self.user, self.movie, self.stars)
