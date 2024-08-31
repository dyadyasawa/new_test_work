
from rest_framework import serializers  # ModelSerializer, SerializerMethodField

from users.models import User
from users.validators import ValidatePasswordSymbolsCount


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        validators = [ValidatePasswordSymbolsCount(field="password")]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
