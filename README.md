### YATUBE API

## Описание
#### Польза проекта в том, что он дает пользоваться функционалом приложения не посещая сайт.
##### Реализован функционал дающий возможность:
* Подписываться на пользователя.
* Просматривать, создавать новые, удалять и изменять посты.
* Просматривать и создавать группы.
* Комментировать, смотреть, удалять и обновлять комментарии.
* Фильтровать по полям.

#### К API есть документация по адресу `http://localhost:8000/redoc/`

### Установка:
-настройте виртуальное окружение
    ```
    python3 -m venv venv_name
    ```
-установите необходимые зависимости
    ```
    pip install -r requirements.txt
    ```
- запустите проект
    ```
    python manage.py runserver
    ```


### Пример запроса к API:
```
/api/v1/posts/   (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/<id>   (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/<id>/comments  (GET, POST, PUT, PATCH, DELETE)
/api/v1/posts/<id>/comments/<id>  (GET, POST, PUT, PATCH, DELETE)
/api/v1/group/ (GET, POST)
/api/v1/follow/  (GET, POST)
```
