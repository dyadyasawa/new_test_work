
from datetime import date

from rest_framework.serializers import ValidationError

from users.models import User


def validate_count_symbols_in_password(value):
    pass
    # """ Валидация по длине пароля. """
    # symbols_count = len(User.password)
    #
    # if symbols_count < 8:
    #     raise ValidationError("Слишком короткий пароль")
