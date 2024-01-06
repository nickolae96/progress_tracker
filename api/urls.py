from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from api import views

router = routers.DefaultRouter()
router.register(r'register', views.RegisterViewSet, basename='register')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'activity_items', views.ActivityItemViewSet, basename='activity_item')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]