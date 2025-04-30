
# 🛡️ Insurance Backend

Бекенд-частина інформаційної системи автострахування.

## 📋 Опис проєкту

Ця система дозволяє користувачам реєструватися, авторизуватися та оформлювати страхові поліси онлайн.
Агенти можуть переглядати всі поліси у системі.

---

## 🛠 Використані технології

- Python 3.12 (Для Linux - Python 3.10)
- Django 5.x
- Django REST Framework
- PostgreSQL
- JWT авторизація (djangorestframework-simplejwt)

---

## 🚀 Як запустити проєкт локально

1. Клонуйте репозиторій:

```bash
git clone https://github.com/Hallcuon/insurance-backend.git
cd insurance-backend
```

2. Створіть та активуйте віртуальне середовище:

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```
- - - ЯКЩО СКРИПТ НЕ ЗАПУСКАЄТЬСЯ - ПОТРІБНО ЗНЯТИ ОБМЕЖЕННЯ ВИКОНАННЯ СКРИПТІВ В PowerShell
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

3. Встановіть залежності:

```bash
pip install -r requirements.txt
```

4. Налаштуйте базу даних PostgreSQL у settings.py.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'НАЗВА БД',
        'USER': 'postgres', 
        'PASSWORD': 'ПАРОЛЬ ВІД БД',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

6. Виконайте міграції:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Запустіть сервер:

```bash
python manage.py runserver
```

---

## 📚 Основні API-ендпоїнти

| Шлях | Метод | Опис |
|:---|:---|:---|
| `/api/register/` | POST | Реєстрація користувача |
| `/api/token/` | POST | Отримання JWT токену |
| `/api/token/refresh/` | POST | Оновлення access токену |
| `/api/policies/` | GET | Перегляд полісів |
| `/api/policies/` | POST | Створення нового поліса |

---

## 🛡️ Аутентифікація

Всі захищені запити потребують заголовок:

```
Authorization: Bearer <Ваш access_token>
```

---

## 📌 Статус проєкту

✅ Бекенд повністю реалізований та готовий для підключення фронтенду на React.  
✅ Успішно протестовано через Postman.  
✅ Реалізовано розмежування прав доступу: клієнти бачать свої поліси, агенти — всі.

---
