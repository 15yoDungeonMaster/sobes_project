# sobes_project
________________________________________________________________

## Описание

Данный софт предназначен для учета сотрудников, представляет собой связанные модели `Person` и `Subordination` с возможностью выполнения CRUD операций над ними и аутентификацией с помощью JWT

________________________________________________________________
## Установка

1. Перейти в папку с проектом и выполнить установку зависимостей командой `pip install -r requirements.txt`
2. Создать и применить миграции командами `python manage.py makemigrations` и `python manage.py migrate`
3. Для использования админки требуется создать суперюзера(админа) командой `python manage.py createsuperuser` и следовать инструкциям в терминале

При возникновении ошибки `ModuleNotFoundError: No module named 'pkg_resources'`, требуется обновить сборщик командой `python3 -m pip install --upgrade pip setuptools`

Для наглядности работы предусмотрены фикстуры, для их установки нужно выполнить команду `python manage.py loaddata employee_records/fixtures/initial_data.json`
________________________________________________________________
