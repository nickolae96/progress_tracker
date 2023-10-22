from django.contrib.auth.models import User
from rest_framework import viewsets, mixins

from api.serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.get_queryset()

