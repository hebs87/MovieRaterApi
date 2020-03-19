from django.urls import include, path
from rest_framework import routers

# Use router to register our ViewSets as urls (REST framework)
router = routers.DefaultRouter()

urlpatterns = [
    # Create a path to include our router urls
    path('', include(router.urls))
]
