# API для Yatube

## Описание

**Yatube** — социальная сеть для публикации записей. Этот проект — REST API для неё:
через API можно публиковать посты, комментировать их, просматривать сообщества
и подписываться на авторов. API пригодится для мобильного приложения, бота или
любого другого клиента.

Возможности:
- публикации (CRUD, пагинация через `limit`/`offset`);
- комментарии к публикациям (CRUD);
- сообщества (только чтение);
- подписки на авторов (просмотр своих подписок с поиском `?search=`, оформление подписки);
- аутентификация по JWT-токенам (Djoser + Simple JWT).

Права доступа:
- аноним — только чтение (кроме `/follow/` — для него 401);
- аутентифицированный пользователь — создание контента, изменение и удаление **своего** контента.

Стек: Python 3.10, Django 3.2, Django REST Framework 3.12, Simple JWT, Djoser.

## Установка

```bash
git clone https://github.com/<ваш-аккаунт>/api_final_yatube.git
cd api_final_yatube
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cd yatube_api
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Документация: http://127.0.0.1:8000/redoc/

Тесты (из корня репозитория): `pytest`

## Примеры запросов

Получить токен:
```
POST /api/v1/jwt/create/
{"username": "user", "password": "password"}
```
Ответ: `{"refresh": "...", "access": "..."}`. Дальше передавайте заголовок
`Authorization: Bearer <access>`.

Создать публикацию:
```
POST /api/v1/posts/
{"text": "Мой первый пост", "group": 1}
```

Список публикаций с пагинацией:
```
GET /api/v1/posts/?limit=10&offset=0
```

Добавить комментарий:
```
POST /api/v1/posts/1/comments/
{"text": "Отличный пост!"}
```

Подписаться на автора:
```
POST /api/v1/follow/
{"following": "author_username"}
```

Найти подписку:
```
GET /api/v1/follow/?search=author
```
