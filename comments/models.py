
from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now_add=True, verbose_name='Дата редактирования')

    def __str__(self):
        return f'{self.author}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
