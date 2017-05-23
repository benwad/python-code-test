from django.db import models
from django.contrib.auth.models import User

from episodes.models import Episode


class AbstractReaction(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()
    episode = models.ForeignKey(Episode, null=True, blank=False)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class ImageReaction(AbstractReaction):
    image = models.ImageField()


class TweetReaction(AbstractReaction):
    text = models.CharField(max_length=150)
