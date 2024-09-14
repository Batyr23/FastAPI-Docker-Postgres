# FastAPI CRUD Project with Analytics

## Описание проекта

Этот проект представляет собой веб-приложение, разработанное с использованием **FastAPI** для создания, чтения, обновления и удаления (CRUD) записей в базе данных. Проект также включает визуализацию данных на главной странице с использованием библиотеки **Chart.js**, где представлена аналитика данных. Приложение взаимодействует с базой данных через **SQLAlchemy**, а схемы данных валидируются с помощью **Pydantic**.

## Основные возможности

- CRUD-операции с записями в базе данных через API.
- Визуализация данных на главной странице:
  - Общее количество записей
  - Количество активных записей
  - Линейный график, показывающий динамику создания записей по дате
- Форма для добавления новых записей через веб-интерфейс.

## Структура проекта

Проект состоит из следующих ключевых файлов и папок:

### 1. `main.py` — Основной файл приложения
Этот файл является точкой входа в приложение и содержит определение маршрутов (API эндпоинтов), которые обрабатывают CRUD-операции и отображение визуализаций.

- **Маршруты**:
  - `/add/`: Обработчик для добавления новой записи в базу данных.
  - `/tp_dicts_view/`: Отображение всех записей с поддержкой удаления и обновления.
  - `/analytics/`: Эндпоинт для получения аналитических данных о записях в базе.
  
- **Функции**:
  - Создание сессии базы данных через зависимости (`Depends`).
  - Взаимодействие с другими компонентами, такими как схемы и функции для работы с базой данных.

### 2. `schemas.py` — Pydantic-схемы
Этот файл содержит схемы для валидации данных, которые приходят и отправляются через API. Схемы помогают убедиться, что данные, которые приходят от клиента (например, через JSON), соответствуют нужной структуре и типам данных.

- **TpDictBase**: Базовая схема для записи с полями `tp_code`, `tp_name`, `tp_status`, `is_commercial`, `valid_from`, `valid_to`.
- **TpDictCreate**: Схема для создания новой записи.
- **TpDictUpdate**: Схема для обновления записи.
- **TpDictOut**: Схема для возврата данных записи, включая метаданные (дата создания и обновления).

### 3. `models.py` — SQLAlchemy-модели
Здесь описана структура таблиц в базе данных. Используются модели для управления данными, которые будут храниться в базе данных.

- **TpDict**: Модель для таблицы `tp_dict`, которая содержит такие поля, как `tp_code`, `tp_name`, `created_at`, и `updated_at`. Это основная таблица для хранения данных, с которыми работает приложение.

### 4. `crud.py` — Операции с базой данных (CRUD)
Этот файл содержит функции для работы с базой данных через SQLAlchemy. Здесь описаны операции для создания, чтения, обновления и удаления записей.

- **create_tp_dict**: Функция для создания новой записи.
- **get_tp_dicts**: Функция для получения списка записей.
- **get_tp_dict**: Получение одной записи по `tp_code`.
- **update_tp_dict**: Обновление записи.
- **delete_tp_dict**: Удаление записи.

### 5. `database.py` — Настройки базы данных
Этот файл управляет подключением к базе данных с использованием SQLAlchemy. Он содержит конфигурацию для подключения к базе и функции для управления сессиями.

## Используемые технологии

- **FastAPI** — Фреймворк для разработки API.
- **SQLAlchemy** — ORM для работы с базой данных.
- **Pydantic** — Валидация данных.
- **Chart.js** — Визуализация данных на фронтенде.
- **Jinja2** — Шаблонизатор для рендеринга HTML.

## Запуск проекта
