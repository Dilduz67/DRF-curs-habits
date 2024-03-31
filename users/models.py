from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'null': True, 'blank': True}

# Определение модели пользователей, наследующей абстрактную модель пользователя
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Адрес электронной почты пользователя")
    telegram_chat_id = models.IntegerField(unique=True, default=None, **NULLABLE)
    telegram_user_name = models.CharField(max_length=100, unique=True, **NULLABLE)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = 'пользователи'