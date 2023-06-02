FROM python:3.11-slim

# Копируем файлы poetry в контейнер
WORKDIR /app
COPY pyproject.toml poetry.lock ./

# Устанавливаем Poetry и зависимости
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-dev

# Копируем остальные файлы проекта в контейнер
COPY . .

# Устанавливаем переменную окружения
ENV FASTAPI_ENV=production

# Запуск приложения
CMD python run.py