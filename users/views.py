from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializer import UserSerializer


def get_object(id):
    try:
        return User.objects.get(pk=id)
    except User.DoesNotExist:
        raise NotFound()


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def ListUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def RegisterUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetUser(request, id):
    user = get_object(id)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def DeleteUser(request):
    user = get_object(request.user.id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
