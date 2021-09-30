Тестовое задание для компании ООО "Фабрика Решений"


Текст задания:

Задача: спроектировать и разработать API для системы опросов пользователей.

Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

Использовать следующие технологии: Django 2.2.10, Django REST framework.


----------------------------------------------------------------


Инструкция по разворачиванию проекта локально:
1. Установить Python 3.6+
2. Установить Git
3. Устновить PostgreSQL 9+
4. Открыть консоль/терминал
5. Создать виртуальное пространство для проекта командой `virtualenv название_пространства`
6. Активировать виртуальное пространство
  6.1. Для Windows ```cd название_пространства/Scripts
activate
cd ../..```
  6.2. Для Linux ```source название_пространства/bin/activate```
7. Клонировать репозиторий на локальную машину `git clone https://github.com/mykhailokukol/fabrique_test.git`
8. Установить зависимости `pip install -r requirements.txt`
  8.1. Для Linux отдельно установить psycopg2-binary версии 2.8.6 `pip install psycopg2-binary==2.8.6`
9. Создать файл .env и вписать в него название базы данных, имя пользователя и пароль
```
DB_NAME = 'название'
DB_USER = 'имя_пользователя'
DB_USER_PASSWORD = 'пароль'
```
10. Перейти в папку с проектом `cd project` и запустить его `python manage.py runserver [порт]` (можно также указать порт, на котором запустится проект)
11. Открыть браузер, ввести в адресную строку адрес локальной машины и порт через двоеточие (например, `localhost:8000`, если не указывать порт вручную)


------------------------------------------------


Документация по API

Для получения GUI с API проекта, перейдите по адресу `localhost:8000/api/`.
На открывшейся странице будет 3 объекта: quizes, questions, answers.

quizes:
  Ссылка на все хранимые объекты (строки) модели (таблицы) "Опросы". Каждый опрос содержит в себе ссылки на "Вопросы" и "Ответы";
questions:
  Ссылка на все хранимые объекты модели "Вопросы";
answers:
  Ссылка на все хранимые объекты модели "Ответы";

При нажатии на ссылку любой модели откроется новая страница, содержащая подробную информацию о каждом объекте отдельно.

Также в API содержится информация о пагинации GUI: "count" - количество объектов на странице, "next" - следующая страница, "previous" - предыдущая страница.