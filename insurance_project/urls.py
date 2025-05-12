from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Адмін-панель
    path('api/', include('insurance.urls')),  # Підключення маршрутів додатку insurance
]