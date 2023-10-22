from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from api.models import UserPhoto


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
