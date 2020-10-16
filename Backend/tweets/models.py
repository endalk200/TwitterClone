from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Tweets(models.Model):
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # TODO: add additional fields

    objects = models.Manager()

    class Meta:
        ordering = ['-id']

    def __str__(self, *args, **kwargs) -> str:
        """
        string representation of the class
        """
        return f"Tweet ID: { self.pk } | Tweet Timestamp: { self.timestamp }"