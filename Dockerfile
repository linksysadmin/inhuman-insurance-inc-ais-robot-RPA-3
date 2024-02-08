FROM python:3.10

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Install dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Копирование вашего проекта в контейнер
COPY . /app

# CMD для запуска вашего скрипта
CMD ["python", "producer.py"]