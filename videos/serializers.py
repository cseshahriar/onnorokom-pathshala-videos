from rest_framework import serializers
from .models import Video, Like, Dislike


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'youtube_video_id',
            'author_id',
            'like_list',
            'dislike_list',
            'view_count',
            'created_at'
        ]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'video', 'user_id', 'created_at']


class DisLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ['id', 'video', 'user_id', 'created_at']
