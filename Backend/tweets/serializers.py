from rest_framework import serializers

from tweets.models import Tweets


class TweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = ['id', 'content', 'timestamp']
