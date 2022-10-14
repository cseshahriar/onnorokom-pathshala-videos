# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Video, like, Dislike


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'title',
        'slug',
        'description',
        'youtube_video_id',
        'author_id',
        'view_count',
        'is_active',
    )
    list_filter = ('created_at', 'updated_at', 'is_active')
    search_fields = ('slug',)
    date_hierarchy = 'created_at'


@admin.register(like)
class likeAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'video', 'user_id')
    list_filter = ('created_at', 'updated_at', 'video')
    date_hierarchy = 'created_at'


@admin.register(Dislike)
class DislikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'video', 'user_id')
    list_filter = ('created_at', 'updated_at', 'video')
    date_hierarchy = 'created_at'
