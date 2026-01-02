from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    register_view,
    profile_view,
    logout_view,
    EmailTokenObtainPairView,
)

urlpatterns = [
    path("register/", register_view),
    path("profile/", profile_view),
    path("logout/", logout_view),
    path("token/", EmailTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]