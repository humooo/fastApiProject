# Веб-сервис для управления товарами и категориями товаров

Этот проект представляет собой простой веб-сервис, предоставляющий RESTful API для управления товарами и категориями товаров. Веб-сервис реализован с использованием FastAPI и SQLAlchemy с базой данных SQLite.

## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone git@github.com:humooo/fastApiProject.git
   cd fastApiProject
   ```

2. **Создайте виртуальное окружение:**

   ```bash
   python -m venv venv
   ```

3. **Активируйте виртуальное окружение:**

   - Для Windows:

     ```bash
     venv\Scripts\activate
     ```

   - Для macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

## Запуск приложения

Для запуска веб-сервиса используйте команду:

```bash
uvicorn main:app --reload
```

## API Эндпоинты

### Категории товаров

- **Создать категорию:**

  ```
  POST /categories/
  ```

  Тело запроса:
  ```json
  {
      "name": "Название категории",
      "description": "Описание категории (необязательно)"
  }
  ```

- **Получить все категории:**

  ```
  GET /categories/
  ```

- **Получить категорию по ID:**

  ```
  GET /categories/{category_id}
  ```

### Товары

- **Создать товар:**

  ```
  POST /products/
  ```

  Тело запроса:
  ```json
  {
      "name": "Название товара",
      "description": "Описание товара",
      "price": 100.0,
      "category_id": 1
  }
  ```

- **Получить все товары:**

  ```
  GET /products/
  ```

- **Получить товар по ID:**

  ```
  GET /products/{product_id}
  ```

## Технологии

- **FastAPI**: для создания API
- **SQLAlchemy**: для работы с базой данных
- **SQLite**: в качестве базы данных
