
from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    login = models.CharField(max_length=150, unique=True, verbose_name="Логин")
    password = models.CharField(max_length=128, unique=True, verbose_name="Пароль")
    phone = models.CharField(max_length=25, verbose_name="Телефон", **NULLABLE)
    date_of_birth = models.DateField(default="2000-01-01", verbose_name='Дата рождения')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now_add=True, verbose_name='Дата редактирования')

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.login}"
