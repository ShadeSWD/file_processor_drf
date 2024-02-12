# Загрузка и обработка файлов

``Django REST API``, который позволяет загружать файлы на сервер, а затем асинхронно обрабатывать их с использованием ``Celery``.

**Основные задачи:**

- [x] Модель ``file``
- [x] Сериализатор модели ``file``
- [x] Эндпоинт ``upload/`` для загрузки файлов
- [x] ``Celery`` задача для обработки файла
- [x] Эндпоинт ``files/`` для получения данных загруженных файлов

**Задачи "CI/CD":**

- [x] Тесты
- [ ] docker
- [x] Базовый CI/CD - проверка кода линтерами (``flake8``) и форматерами (``black``, ``isort``)

**Запуск проекта:**
* перед запуском убедитесь, что у вас установлен ``redis``
* Склонируйте репозиторий:
    ```bash
    git clone https://github.com/ShadeSWD/file_processor_drf.git
    ```
* Установите пакетный менеджер poetry:
    ```bash
    pip install poetry
    ```
* Создайте базу данных в ``PostgreSQL`` и заполните файл ``.env``, воспользовавшись ``.env.sample``
* Перейдите в папку с проектом и настройте виртуальное окружение
    ```bash
    poetry install
    ```
* Войдите в виртуальное окружение
    ```bash
    poetry shell
    ```
* Накатите миграции:
  ```bash
  manage.py migrate
  ```
* Создайте суперпользователя:
  ```bash
  manage.py createsuperuser
  ```
* Запустите сервер:
    ```bash
    manage.py runserver
    ```
* В другой консоли необходимо перейти в корень проекта, активировать виртуальную среду и запустить celery:
  ```bash
  celery -A config worker --loglevel=info -P eventlet
  ```
* Домашняя страница будет доступна по адресу вашего хоста
* Перед первым коммитом необходимо выполнить
  ```bash
  pre-commit install
  ```
  для автоматического выполнения проверок перед коммитами

## Основные задачи

### Эндпоинт для загрузки файлов

Эндпоинт ``upload/``, принимает POST-запросы для загрузки файлов. При загрузке файла создаётся объект модели File, и файл сохраняется на сервере. В ответ на успешную загрузку файла вернуть статус 201 и сериализованные данные файла.

После загрузки файла запускается фоновая задача обработки

Пример ответа:
```
{
  "pk": 7,
  "upload_at": "2024-02-11T22:51:23.537462Z",
  "processed": false,
  "processed_at": null
}
```

### Эндпоинт для получения данных обо всех загруженных файлах

Эндпоинт ``files/``, принимает пустой GET-запрос и возвращает список всех файлов с их данными.

### Отложенная задача обработки файлов

После загрузки каждого файла запускается отложенная задача обработки файла. После выполнения задачи поля файла ``processed`` меняется на ``True``, а полю ``procedssed_at`` присваиваются дата и время окончания обработки.

## Задачи "CI/CD"

### Тесты
* Для запуска тестов необходимо находясь в корне проекта активировать виртуальное окружение
    ```bash
    poetry shell
    ```
* запустите тесты:
  ```bash
  manage.py test
  ```
* для просмотра отчета о покрытии тестами выполните
  ```bash
  coverage run --source='.' manage.py test
  coverage report
  ```
