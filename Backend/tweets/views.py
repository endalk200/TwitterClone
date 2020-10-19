
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions

from knox.auth import TokenAuthentication

from .serializers import TweetsSerializer
from .models import Tweets


class CreateTweet(APIView):
    """
    Create new tweet
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = TweetsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TweetsList(APIView):
    """
    List all tweets created
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        tweets = Tweets.objects.all()
        serializer = TweetsSerializer(tweets, many=True)
        return Response(serializer.data)


class TweetDetail(APIView):
    """
    Retrieve all details related to a specific tweet
    """

    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return Tweets.objects.get(pk=pk)
        except Tweets.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tweet = self.get_object(pk=pk)
        serializer = TweetsSerializer(tweet)
        return Response(serializer.data)


class UpdateTweet(APIView):
    """
    Update a given tweet
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Tweets.objects.get(pk=pk)
        except Tweets.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        tweet = self.get_object(pk)
        serializer = TweetsSerializer(tweet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteTweet(APIView):
    """
    Delete the tweet and all associated resources
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Tweets.objects.get(pk=pk)
        except Tweets.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        tweet = self.get_object(pk=pk)
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
