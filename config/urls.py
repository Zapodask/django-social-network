from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from posts.views import PostsViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
