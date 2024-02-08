# Базовый образ Miniconda
FROM continuumio/miniconda3:latest

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование файла conda.yaml в контейнер
COPY conda.yaml /app

# Обновление Conda и создание Conda окружения
RUN conda update -n base -c defaults conda && \
    conda env create -f conda.yaml

# Активация Conda окружения
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
RUN echo "source activate myenv" > ~/.bashrc

# Копирование вашего проекта в контейнер
COPY . /app

# CMD для запуска вашего скрипта (заменить на ваш файл скрипта)
CMD ["conda", "run", "-n", "myenv", "python", "producer.py"]