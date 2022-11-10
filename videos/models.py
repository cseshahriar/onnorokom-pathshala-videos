from django.db import models
from .utils import generate_unique_slug
from django.utils.text import slugify
from users.models import User


class BaseAttribute(models.Model):
    created_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="%(app_label)s_%(class)s_created_by"
    )
    updated_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="%(app_label)s_%(class)s_updated_by"
    )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Video(BaseAttribute):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    description = models.TextField(max_length=300)
    youtube_video_id = models.CharField(max_length=255)
    view_count = models.BigIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    @property
    def like_list(self):
        return self.likes.all()

    @property
    def like_count(self):
        return self.like_list.count()

    @property
    def dislike_list(self):
        return self.dislikes.all()

    @property
    def dislike_count(self):
        return self.dislike_list.count()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Video, self.title)
        else:  # create
            self.slug = generate_unique_slug(Video, self.title)
        super(Video, self).save(*args, **kwargs)


class Like(BaseAttribute):
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE,
        related_name='likes'
    )

    class Meta:
        unique_together = (('created_user', 'video'),)
        index_together = (('created_user', 'video'),)

    def __str__(self):
        return self.video.title


class Dislike(BaseAttribute):
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE,
        related_name='dislikes'
    )

    class Meta:
        unique_together = (('created_user', 'video'),)
        index_together = (('created_user', 'video'),)

    def __str__(self):
        return self.video.title
