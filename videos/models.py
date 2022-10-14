from django.db import models
from .utils import generate_unique_slug
from django.utils.text import slugify


class BaseAttribute(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Video(BaseAttribute):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    description = models.TextField(max_length=300)
    youtube_video_id = models.CharField(max_length=255)
    author_id = models.BigIntegerField()
    view_count = models.BigIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    @property
    def like_list(self):
        return self.likes.all()

    @property
    def dislike_list(self):
        return self.dislikes.all()

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
    user_id = models.PositiveIntegerField()

    class Meta:
        unique_together = (('user_id', 'video'),)
        index_together = (('user_id', 'video'),)

    def __str__(self):
        return self.video.title


class Dislike(BaseAttribute):
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE,
        related_name='dislikes'
    )
    user_id = models.PositiveIntegerField()

    class Meta:
        unique_together = (('user_id', 'video'),)
        index_together = (('user_id', 'video'),)

    def __str__(self):
        return self.video.title
