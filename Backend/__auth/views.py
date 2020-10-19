from django.utils import timezone

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions

from knox.settings import knox_settings
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.views import LoginView, LogoutAllView

from django.contrib.auth.models import User

from .serializers import UserSerializer, SignUpSerializer


class CreateUser(APIView):
    """ 
    Create new user with user data provided
    """

    def post(self, request, format=None):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            # AuthToken return tuple object
            _, token = AuthToken.objects.create(user)

            return Response({
                "user": UserSerializer(user).data,
                "token": token
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(LoginView):
    # overide TOKEN_lIMIT
    CUSTOM_TOKEN_LIMIT_PER_USER = None # TODO: implement Token clean up action

    def get_token_limit_per_user(self):
        return self.CUSTOM_TOKEN_LIMIT_PER_USER

    def get_user_serializer_class(self):
        """
        overide the UserSerializer that will be used to return user data
        after the user successfully logs in
        """
        return UserSerializer
