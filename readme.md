# sobes_project
________________________________________________________________

## Описание

Данный софт предназначен для учета сотрудников, представляет собой связанные модели `Person` и `Subordination` с возможностью выполнения CRUD операций над ними и аутентификацией с помощью JWT

________________________________________________________________
## Установка

1. Перейти в папку с проектом и выполнить установку зависимостей командой `pip install -r requirements.txt`
2. Создать и применить миграции командами `python manage.py makemigrations` и `python manage.py migrate`

Для наглядности работы предусмотрены фикстуры, для их установки нужно выполнить команду `python manage.py loaddata employee_records/fixtures/initial_data.json`
________________________________________________________________