
from rest_framework import serializers  # ModelSerializer, SerializerMethodField

from users.validators import validate_age
from users.models import User
# from users.validators import validate_count_symbols_in_password


class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(validators=[validate_count_symbols_in_password])
    date_of_birth = serializers.DateField(validators=[validate_age])

    class Meta:
        model = User
        fields = "__all__"
