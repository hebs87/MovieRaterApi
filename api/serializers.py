from rest_framework import serializers
from .models import Movie, Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    """
    A serializer to serialize the user data and create a new
    user record in the database (registration functionality)
    """
    class Meta:
        model = User
        # The password is automatically hashed
        fields = ('id', 'username', 'password')
        # We use the extra_kwargs for the password field to make it a write-only field (won't
        # be visible in the database), but a required field (required to login)
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        # We call the create_user method on the User object and pass in the validated_data
        # with the extra_kwargs
        user = User.objects.create_user(**validated_data)
        # We create a Token and assign it to the user
        Token.objects.create(user=user)
        return user


class MovieSerializer(serializers.ModelSerializer):
    """
    A serializer to serialize the data passed into the
    Movie model
    """
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_rating')


class RatingSerializer(serializers.ModelSerializer):
    """
    A serializer to serialize the data passed into the
    Rating model
    """
    class Meta:
        model = Rating
        fields = ('id', 'movie', 'user', 'stars')
