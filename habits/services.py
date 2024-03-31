from datetime import timedelta, timezone

from config import settings
from habits.models import Habit
import requests

from users.models import User

# Получение токена для API Telegram из настроек проекта
TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN

def send_telegram_messages():
    today = timezone.now()
    for user in User.objects.all():
        if User.id==Habit.user:
            for obj in Habit.objects.all():
                if obj.time == today:
                    params = {'chat_id': user.telegram_chat_id,
                              "text": f"Hi, friend, it's time to be active! "
                                      f"Do it right now {obj.action},"
                              }
                    requests.get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage', params=params).json()
                    if obj.periodicity == 'daily':
                        obj.time = today + timedelta(days=1)
                        obj.save()
                    elif obj.periodicity == 'weekly':
                        obj.time = today + timedelta(days=7)
                        obj.save()
                    else:
                        obj.time = today + timedelta(days=3)
                        obj.save()
