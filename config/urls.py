from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from posts.views import PostsViewSet
from users.views import UsersViewSet


router = routers.DefaultRouter()
router.register(r"posts", PostsViewSet)
router.register(r"users", UsersViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("", include(router.urls)),
]
