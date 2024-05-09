# Используем базовый образ Python
FROM python:3.11

# Устанавливает переменную окружения, которая гарантирует, что вывод из python
# будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /DRF-curs-habits

# Копируем зависимости и код приложения
COPY ./requirements.txt .
RUN pip install -r /DRF-curs-habits/requirements.txt
COPY . .

# Команда для запуска Django-сервера
#CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]