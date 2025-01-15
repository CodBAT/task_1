# task_1
Проект создан в учебных целях для демонстрации использования FastAPI и Docker.

# TODO-Service

TODO-Service — это приложение на базе FastAPI для управления списком задач. Оно предоставляет API для создания, чтения, обновления и удаления задач (CRUD).

## Функциональность

- **POST /tasks/**: Создание новой задачи.
- **GET /tasks/**: Получение списка всех задач.
- **GET /tasks/{task_id}**: Получение задачи по ID.
- **PUT /tasks/{task_id}**: Обновление задачи по ID.
- **DELETE /tasks/{task_id}**: Удаление задачи по ID.

Приложение использует SQLite в качестве базы данных.

Структура проекта:

todo-service/
├── main.py            # Основной файл приложения FastAPI
├── crud.py            # Функции для работы с базой данных
├── database.py        # Настройки SQLite
├── models.py          # Описание моделей базы данных
├── requirements.txt   # Зависимости проекта
└── Dockerfile         # Описание для сборки Docker-образа


---

## Запуск проекта

### Запуск локально

#### 1. Установите зависимости
Создайте виртуальное окружение (опционально) и установите зависимости из `requirements.txt`:

pip install -r requirements.txt

### Запуск через Docker

Скачайте образ из Docker Hub:

https://hub.docker.com/repositories/codebat1

Запустите контейнер с образом:

docker run -d -p 8000:80 codebat1/todo-service:latest

Откройте в браузере:

http://<ваш_публичный_IP>:8000/docs




