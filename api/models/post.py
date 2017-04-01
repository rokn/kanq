from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from .rating import Rating
from .image import Image
from .topic import Topic
from .tag import Tag
from .user import User


class Post(models.Model):
    description = models.TextField(max_length=500)
    title = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_creator')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='post_topic')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='post_image')
    tags = models.ManyToManyField(Tag, related_name='post_tags')
    ratings = GenericRelation(Rating, related_name='post_ratings')

    def __str__(self):
        return self.title

