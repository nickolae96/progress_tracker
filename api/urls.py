from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from api.views import MyTokenObtainPairView, RegisterViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]