from datetime import date

from rest_framework.serializers import ValidationError

forbidden_words = ["ерунда", "глупость", "чепуха"]


def validate_forbidden_words(value):
    """ Валидация по запрещенным словам. """
    if value.lower() in forbidden_words:
        raise ValidationError("В заголовке использовано запрещенное слово")


class ValidateAge:
    """ Валидация по возрасту. """

    def __init__(self, field):
        self.field = field

    def __call__(self, post):
        today = date.today()

        if today.year - post.get("author").date_of_birth.year < 18:
            raise ValidationError("Маловато годиков")
        # if value.get("author"):
        #     today = date.today()
        #     age = today.year - value.date_of_birth.year
        #     print(age)
        #     if age < 18:
        #         raise ValidationError("Маловато годиков")
        #     return None
