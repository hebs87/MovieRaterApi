from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Movie(models.Model):
    """
    A model to hold the movie details
    """
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)


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
