from datetime import timedelta

from django.utils import timezone

from config import settings
from habits.models import Habit
import requests

from users.models import User

# Получение токена для API Telegram из настроек проекта
TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN

def send_telegram_messages():
    today = timezone.now().date()
    """рассылаем сообщения всем пользователям"""
    for user in User.objects.all():
        for obj in Habit.objects.all():
            if  Habit.time.date() <= today:
                habit_time = Habit.time.time().strftime("%H:%M")
                params = {'chat_id': user.telegram_chat_id,
                          "text": f"Hi, friend, it's time to be active! "
                                  f"Do {obj.action} at {habit_time},"
                          }
                requests.get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage', params=params).json()

    """записываем время следующего выполнения"""
    for obj in Habit.objects.all():
        if obj.periodicity == 'daily':
            obj.time = obj.time + timedelta(days=1)
            obj.save()
        elif obj.periodicity == 'weekly':
            obj.time = obj.time + timedelta(days=7)
            obj.save()
