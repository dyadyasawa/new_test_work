
from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Post(models.Model):
    header = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    image = models.ImageField(upload_to='post/', verbose_name='Изображение', **NULLABLE)

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now_add=True, verbose_name='Дата редактирования')

    def __str__(self):
        return f'{self.header}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
