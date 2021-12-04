from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import ListUsers, RegisterUser, DeleteUser, GetUser


urlpatterns = [
    path("", ListUsers),
    path("register", RegisterUser),
    path("<int:id>", GetUser),
    path("delete-my-user", DeleteUser),
    path("login", TokenObtainPairView.as_view()),
    path("refresh-token", TokenRefreshView.as_view()),
]
