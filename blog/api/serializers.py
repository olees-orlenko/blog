from posts.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("id",)
