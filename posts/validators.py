
from rest_framework.serializers import ValidationError

forbidden_words = ["ерунда", "глупость", "чепуха"]


def validate_forbidden_words(value):
    """ Валидация по запрещенным словам. """
    if value.lower() in forbidden_words:
        raise ValidationError("В заголовке использовано запрещенное слово")
