from rest_framework import viewsets

from posts.models import Post
from posts.serializer import PostSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
