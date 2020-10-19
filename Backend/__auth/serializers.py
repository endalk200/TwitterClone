from rest_framework import serializers

from django.contrib.auth.models import User

from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to be used when the user is created an account for the first
    time. The user data in this serializer will be returned to the 
    authenticated user
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserDataSerializer(serializers.ModelSerializer):
    """
    Serializer to represent a users full information only authenticated user
    can access this serializer
    """
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 
            'date_joined', 'last_login'
        ]


class SignUpSerializer(serializers.ModelSerializer):
    """
    Serializer for sign up process with two field and some validation workflow
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def created(self, validated):
        """
        method that will be called after the all data provided are validated
        """
        user = User.objects.create_user(**validated)
        return user