from django.urls import path, include  # noqa
from rest_framework import routers
from .views import VideoViewSet

# routers
router = routers.DefaultRouter()
router.register('videos', VideoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
