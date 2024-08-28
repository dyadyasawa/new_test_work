
from rest_framework import serializers  # ModelSerializer, SerializerMethodField

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
