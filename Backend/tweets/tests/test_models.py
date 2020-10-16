
from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from tweets.models import Tweets

from django.db import models

User = get_user_model()


class TweetsTestCase(TestCase):
    """
    Unit test for Tweets model
    """

    def setUp(self):
        pass

    def test_Tweets_Create(self):
        """
        Test for Tweets model create by creating new tweet
        """

        content = "Hi, There all of you"

        tweet = Tweets.objects.create(
            content = content
        )
        tweet.save()

        tweet_1 = Tweets.objects.get(pk=1)
        self.assertEqual(tweet_1.content, content)

    def test_Tweets_Update(self):
        """
        Test for Tweets model update by creating new tweet and updating it
        """

        first_content = "Hi, There all of you"
        updated_content = "Hello World"

        tweet = Tweets.objects.create( content = first_content )
        tweet.save()

        tweet_update = Tweets.objects.get(pk=1)
        tweet_update.content = updated_content
        tweet_update.save()

        __tweet__ = Tweets.objects.get(pk=1)

        self.assertEqual(__tweet__.content, updated_content)


    def test_Tweets_Delete(self):
        """
        Test for Tweets model delete by creating new tweet and deleting it
        """

        content = "Hi, There all of you"

        tweet = Tweets.objects.create( content = content )
        tweet.save()

        tweet_1 = Tweets.objects.get(pk=1)
        tweet_1.delete()

        self.assertEqual(Tweets.objects.all().count(), 0)
