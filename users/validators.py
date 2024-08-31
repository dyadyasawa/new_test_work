
from rest_framework.serializers import ValidationError

from users.models import User


class ValidatePasswordSymbolsCount:

    def __init__(self, field):
        self.field = field

    def __call__(self, user):

        password = user.get("password")
        if len(password) < 8:
            raise ValidationError("Слишком короткий пароль (нужно не менее 8-ми символов)")

        if not any(ch.isdigit() for ch in password):
            raise ValidationError("Пароль должен содержать цифры")
