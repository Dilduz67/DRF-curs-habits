from celery import shared_task
from habits.services import send_telegram_messages

@shared_task
def tg_send_message():
    send_telegram_messages()  #Посылает сообщение в телеграм, когда надо выполнить активность.

