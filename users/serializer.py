from rest_framework import serializers
from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
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
