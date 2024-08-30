
from datetime import date

from rest_framework.serializers import ValidationError

from users.models import User


def validate_age(value):
    """ Валидация по возрасту. """
    today = date.today()
    age = today.year - value.year
    if age < 18:
        raise ValidationError("Маловато годиков")


def validate_count_symbols_in_password(value):
    pass
    # """ Валидация по длине пароля. """
    # symbols_count = len(User.password)
    #
    # if symbols_count < 8:
    #     raise ValidationError("Слишком короткий пароль")
