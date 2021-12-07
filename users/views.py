from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from users.models import User, Friends
from users.serializer import UserSerializer, FriendsSerializer


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


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetFriends(request, id):
    friends = Friends.objects.get(owner=id)
    serializer = FriendsSerializer(friends)

    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def AddFriends(request):
    data = request.data
    data_users = data.get("users")
    user_id = request.user.id

    data["owner"] = user_id

    try:
        friends = Friends.objects.get(owner=user_id)

        for user in friends.users.all():
            for data_user in data_users:
                if user.id == data_user:
                    return Response(
                        f"you are already friends with user {user.username}",
                        status=status.HTTP_400_BAD_REQUEST,
                    )

        for user in data_users:
            friends.users.add(user)

        serializer = FriendsSerializer(friends)

        return Response(serializer.data)
    except Friends.DoesNotExist:
        serializer = FriendsSerializer(data=data)

        if serializer.is_valid() and user_id not in serializer.data.get("users"):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def RemoveFriends(request):
    data = request.data
    data_users = data.get("users")
    user_id = request.user.id

    try:
        friends = Friends.objects.get(owner=user_id)

        for user in data_users:
            friends.users.remove(user)

        serializer = FriendsSerializer(friends)

        return Response(serializer.data)
    except Friends.DoesNotExist:
        return Response("You do not have friends", status=status.HTTP_400_BAD_REQUEST)
