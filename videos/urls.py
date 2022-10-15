from django.urls import path, include  # noqa
from rest_framework import routers
from .views import (
    VideoViewSet, LikeViewSet, DisLikeViewSet, LikeDeleteAPIView,
    DisLikeDeleteAPIView
)

# routers
router = routers.DefaultRouter()
router.register('videos', VideoViewSet)
router.register('likes', LikeViewSet)
router.register('dislikes', DisLikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('like/delete/', LikeDeleteAPIView.as_view(), name='like_delete_api'),
    path(
        'dislike/delete/', DisLikeDeleteAPIView.as_view(),
        name='dislike_delete_api'
    ),
]
