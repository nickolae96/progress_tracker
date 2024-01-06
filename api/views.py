from django.contrib.auth.models import User, AnonymousUser

from rest_framework import viewsets, mixins
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

from api import serializers
from api import models


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.MyTokenObtainPairSerializer


class RegisterViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = serializers.RegisterSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.get_queryset()


class ActivityViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = serializers.ActivitySerializer
    queryset = models.Activity.objects.get_queryset()

    def get_queryset(self):
        if self.request.user == AnonymousUser.__name__:
            return self.queryset.filter(user=self.request.user)
        else:
            return self.queryset.none()


class ActivityItemViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = serializers.ActivityItemSerializer
    queryset = models.ActivityItem.objects.get_queryset()
