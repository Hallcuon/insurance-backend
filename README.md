# 🛡️ Insurance Backend

Бекенд-частина інформаційної системи автострахування.

---

## 📋 Опис проєкту

Цей застосунок дозволяє:
- користувачам: реєструватися, авторизуватися, створювати страхові поліси онлайн
- агентам: переглядати всі поліси
- адміністраторам: керувати параметрами системи (в перспективі)

Бекенд працює у зв’язці з фронтендом, реалізованим на React.

---

## 🛠 Використані технології

- Python 3.10 / 3.12
- Django 5.x
- Django REST Framework
- PostgreSQL
- JWT авторизація (djangorestframework-simplejwt)
- CORS (django-cors-headers) для роботи з фронтендом

---

## 🚀 Як запустити локально

1. Клонуйте репозиторій:

```bash
git clone https://github.com/твій-нік/insurance-backend.git
cd insurance-backend
```

2. Створіть та активуйте віртуальне середовище:

```bash
python -m venv venv
venv\Scriptsctivate   # або source venv/bin/activate на Linux/Mac
```

> Якщо Windows не дозволяє запуск скриптів — у PowerShell:

```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

3. Встановіть залежності:

```bash
pip install -r requirements.txt
```

4. Налаштуйте PostgreSQL у `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'insurance_db',
        'USER': 'postgres',
        'PASSWORD': 'ваш_пароль',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. Виконайте міграції:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Запустіть сервер:

```bash
python manage.py runserver
```

---

## 🌐 Фронтенд

Фронтенд знаходиться в окремому репозиторії:  
👉 https://github.com/Hallcuon/insurance-frontend

Він автоматично підключається до API http://localhost:8000/api/

---

## 📚 Основні API-ендпоїнти

| Шлях | Метод | Опис |
|:---|:---|:---|
| `/api/register/` | POST | Реєстрація користувача |
| `/api/token/` | POST | Отримання JWT токену |
| `/api/token/refresh/` | POST | Оновлення токену |
| `/api/policies/` | GET | Отримати поліси |
| `/api/policies/` | POST | Створити новий поліс |

---

## 🔐 Аутентифікація

Для захищених запитів:

```http
Authorization: Bearer <ваш access токен>
```

---

## 📌 Статус проєкту

✅ Реалізований повний функціонал бекенду  
✅ Підключено CORS + авторизація  
✅ Працює з React фронтендом  
✅ Покритий тестами, валідовано

---

## 📎 Автор

[Hallcuon]
