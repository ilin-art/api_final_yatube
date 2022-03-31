### YATUBE API

### Описание
Благодаря этому проекту можно делать запросы API к сервису YATUBE и получать необходимую информацию.

### Технологии
Python 3.7
Django 2.2.16

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git
```

```
cd kittygram
```

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
### Примеры запросов API

Получение публикации
```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

Удаление комментария
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

Подписка
```
http://127.0.0.1:8000/api/v1/follow/
```
