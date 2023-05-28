# Yatube API
### Описание
Учебный проект: REST API для сервиса Yatube

### Запуск

Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

### Эндпоинты

- `/api/v1/jwt/create/ (POST)` - получить токен
- `/api/v1/jwt/refresh/ (POST)` - обновить токен
- `/api/v1/jwt/verify/ (POST)` - проверить токен
- `api/v1/posts/ (GET, POST)` - получить список всех постов или создать новый пост
- `api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE)` -  получить/редактировать/удалить пост по id
- `api/v1/groups/ (GET)` -  получить список групп
- `api/v1/groups/{group_id}/ (GET)` - получить информацию о группе по id
- `api/v1/posts/{post_id}/comments/ (GET, POST)` - получить список всех комментариев поста, создать новый комметарий
- `api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE)` - получить/редактировать/ удалить комментарий
- `/api/v1/follow/` (GET, POST) - получить список подписок, добавить новую подписку

### Примеры

1. Получить список постов

- request
```
GET: /api/v1/posts/?limit=10&offset=2
```
- response
```
{
    "count": 8,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "author",
            "image": "http://127.0.0.1:8000/media/posts/images.jpg",
            "text": "post text",
            "pub_date": "2023-05-26T21:59:43.428733Z",
            "group": 1
        }
    ]
}

```
2. Добавить пост
- request
```
POST: /api/v1/posts/

{
  "text": "string",
  "image": "data:image/png;base64,iVBOR..."
  "group": 1
}
```
- response
```
{
    "id": 2,
    "author": "author",
    "image": "http://127.0.0.1:8000/media/posts/temp_uQw7Aap.png",
    "text": "string",
    "pub_date": "2023-05-27T23:08:03.489210Z",
    "group": 1
}
```

3. Получить список подписок
- request
```
GET: /api/v1/follow/?search=au
```
- response
```
[
    {
        "id": 1,
        "user": "user",
        "following": "author"
    },
]
```