from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "author",
            "created_at",
        ]

        extra_kwargs = {
            "created_at": {"read_only": True},
        }

    def create_post(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)

        instance.save()
        return instance

    def validate(self, data):
        if data.get("title") == None:
            raise serializers.ValidationError("The title is required")
        elif data.get("content") == None:
            raise serializers.ValidationError("The content is required")
        else:
            return data
