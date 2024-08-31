
from rest_framework import serializers  # ModelSerializer, SerializerMethodField

from posts.models import Post
from posts.validators import validate_forbidden_words, ValidateAge


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    header = serializers.CharField(validators=[validate_forbidden_words])

    class Meta:
        model = Post
        fields = "__all__"
        validators = [ValidateAge(field="author")]
