# Используем официальный образ Python 3.11
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Выполняем миграции и собираем статические файлы
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Указываем порт
EXPOSE 8000

# Запускаем приложение с Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio.wsgi:application"]