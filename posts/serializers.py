
from rest_framework import serializers  # ModelSerializer, SerializerMethodField

from posts.models import Post
from posts.validators import validate_forbidden_words

from datetime import date


class PostSerializer(serializers.ModelSerializer):
    header = serializers.CharField(validators=[validate_forbidden_words])

    class Meta:
        model = Post
        fields = "__all__"
