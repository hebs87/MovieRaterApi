from django.urls import include, path
from rest_framework import routers
from .views import MovieViewSet, RatingViewSet, UserViewSet

# Use router to register our ViewSets as urls (REST framework)
router = routers.DefaultRouter()
# We register our viewsets
# The first argument is the string that will be passed into the URL path
# The second argument is the viewset itself
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    # Create a path to include our router urls
    path('', include(router.urls))
]
