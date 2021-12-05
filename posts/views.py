from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from posts.serializer import PostSerializer


class Posts(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data["author"] = request.user.id
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostsId(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Post.objects.get(pk=id)
        except Post.DoesNotExist:
            raise NotFound()

    def get(self, request, id):
        post = self.get_object(id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = self.get_object(id)

        if post.author.id == request.user.id:
            request.data["author"] = post.author.id
            serializer = PostSerializer(post, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                "Only the owner can update the post", status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, id):
        post = self.get_object(id)
        if post.author.id == request.user.id:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                "Only the owner can delete the post", status=status.HTTP_400_BAD_REQUEST
            )
