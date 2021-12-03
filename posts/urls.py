from django.urls import path

from posts.views import Posts, PostsId


urlpatterns = [
    path("", Posts().as_view()),
    path("<int:id>/", PostsId().as_view()),
]
