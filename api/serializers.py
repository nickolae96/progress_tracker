from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.models import UserPhoto

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token


class RegisterSerializer(serializers.ModelSerializer):
    photo_url = serializers.URLField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'photo_url']
        extra_kwargs = {'password': {'write_only': True}}

    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        UserPhoto.objects.create(user=user, photo_url=validated_data['photo_url'])
        return user

class UserPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPhoto
        fields = ['photo_url']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'email', 'photo_url']

    def get_photo_url(self, obj):
        try:
            selected_url = UserPhoto.objects.get(user=obj)
        except ObjectDoesNotExist:
            selected_url = None
        return UserPhotoSerializer(selected_url).data['photo_url']
