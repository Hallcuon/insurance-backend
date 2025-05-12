from django.urls import path
from .views import UserRegistrationView, InsurancePolicyView, InsurancePolicyDetailView, HomePageView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Домашня сторінка
    path('register/', UserRegistrationView.as_view(), name='user-register'),  # Реєстрація
    path('policies/', InsurancePolicyView.as_view(), name='policies'),  # Список полісів
    path('policies/<int:id>/', InsurancePolicyDetailView.as_view(), name='policy-detail'),  # Деталі поліса
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT токен
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Оновлення токена
]