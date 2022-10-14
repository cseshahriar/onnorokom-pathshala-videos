from django.urls import path, include  # noqa
from rest_framework import routers
from .views import VideoViewSet, LikeViewSet, DisLikeViewSet

# routers
router = routers.DefaultRouter()
router.register('videos', VideoViewSet)
router.register('likes', LikeViewSet)
router.register('dislikes', DisLikeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
