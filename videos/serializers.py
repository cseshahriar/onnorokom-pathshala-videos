from rest_framework import serializers
from .models import Video, Like, Dislike
from users.serializers import UserSerializer  # noqa


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'video', 'created_user', 'created_at']


class DisLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ['id', 'video', 'created_user', 'created_at']


class VideoSerializer(serializers.ModelSerializer):
    # relational data
    # created_user = UserSerializer(read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    dislikes = DisLikeSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'youtube_video_id',
            'created_user',
            'view_count',
            'created_at',
            'likes',
            'like_count',
            'dislikes',
            'dislike_count'
        ]
