from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.models import User, Friends


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        extra_kwargs = {
            "password": {"write_only": True},
            "date_joined": {"read_only": True},
        }

    def create_user(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.password = validated_data.get("password", instance.password)

        instance.save()
        return instance

    def validate(self, data):
        if data.get("email") == None:
            raise serializers.ValidationError("The email address is required")
        elif data.get("password") == None:
            raise serializers.ValidationError("The password is required")
        else:
            data["password"] = make_password(data["password"])

            return data


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = [
            "owner",
            "users",
        ]

        def update_friends(self, instance, validated_data):
            instance.users = instance.users.pop(validated_data.users.value)

            return instance
