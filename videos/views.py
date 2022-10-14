from rest_framework import status, viewsets  # noqa
from rest_framework.response import Response  # noqa
from rest_framework.decorators import action # noqa
from rest_framework.permissions import IsAuthenticated, AllowAny  # noqa

from .models import Video, Like, Dislike  # noqa
from .serializers import VideoSerializer, LikeSerializer, DisLikeSerializer  # noqa
from rest_framework.authentication import TokenAuthentication  # noqa


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # view count increase if video video detail
        instance.view_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer()
    permission_classes = (AllowAny,)


class DisLikeViewSet(viewsets.ModelViewSet):
    queryset = Dislike.objects.all()
    serializer_class = Dislike()
    permission_classes = (AllowAny,)
