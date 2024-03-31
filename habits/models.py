from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}

class Habit(models.Model):
    PERIODS = [
        ('daily', 'ежедневно'),
        ('weekly', 'раз в неделю'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=100, verbose_name="место для привычки",)
    time = models.TimeField(verbose_name="время для привычки")
    action = models.CharField(max_length=500, verbose_name='действие привычки')

    is_pleasant = models.BooleanField(default=False, verbose_name="Признак приятной привычки",**NULLABLE)
    link_pleasant = models.ForeignKey("self", on_delete=models.CASCADE, **NULLABLE,verbose_name='Ссылка на приятную привычку')

    is_useful = models.BooleanField(default=False, verbose_name="Связанная, полезная привычка", **NULLABLE)

    periodicity = models.CharField(verbose_name="Периодичность", choices=PERIODS, default="daily")
    reward = models.CharField(max_length=500, verbose_name='Вознаграждение', **NULLABLE)
    duration = models.PositiveIntegerField(verbose_name='Время на выполнение')
    is_public = models.BooleanField(verbose_name='Признак публичности', default=False)

    def __str__(self):
        return f'я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
