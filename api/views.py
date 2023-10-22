from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework_simplejwt.views import TokenObtainPairView

from api.serializers import MyTokenObtainPairSerializer, RegisterSerializer, UserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = RegisterSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.get_queryset()
