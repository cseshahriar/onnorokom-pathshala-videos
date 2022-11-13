from rest_framework.views import APIView
from rest_framework import status, viewsets  # noqa
from rest_framework.response import Response  # noqa
from rest_framework.decorators import action # noqa
from rest_framework.permissions import IsAuthenticated, AllowAny  # noqa

from .models import Video, Like, Dislike  # noqa
from .serializers import VideoSerializer, LikeSerializer, DisLikeSerializer
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


class UserVideoListAPIView(APIView):
    """ return user video list"""
    permission_classes = (AllowAny,)

    def get(self, request, user_id, format=None):
        videos = Video.objects.filter(
            created_user_id=user_id).order_by('-created_at')
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (AllowAny,)


class DisLikeViewSet(viewsets.ModelViewSet):
    queryset = Dislike.objects.all()
    serializer_class = DisLikeSerializer
    permission_classes = (AllowAny,)


class LikeDeleteAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        video_id = request.data.get('video')
        user_id = request.data.get('user_id')
        if video_id and user_id:
            Like.objects.filter(
                video_id=video_id, created_user_id=user_id
            ).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class DisLikeDeleteAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        video_id = request.data.get('video')
        user_id = request.data.get('user_id')
        if video_id and user_id:
            Dislike.objects.filter(
                video_id=video_id, created_user_id=user_id
            ).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
