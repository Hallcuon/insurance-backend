# filepath: d:\project\insurance_project\insurance\views.py
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, InsurancePolicy
from .serializers import UserSerializer, InsurancePolicySerializer
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

# Реєстрація користувача
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Список та створення страхових полісів
class InsurancePolicyView(generics.ListCreateAPIView):
    queryset = InsurancePolicy.objects.all()
    serializer_class = InsurancePolicySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_agent:
            return InsurancePolicy.objects.all()
        return InsurancePolicy.objects.filter(client=user)

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

# Видалення або отримання конкретного поліса
class InsurancePolicyDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        """Отримання конкретного поліса"""
        policy = get_object_or_404(InsurancePolicy, id=id)
        if not request.user.is_agent and policy.client != request.user:
            return Response({"error": "Ви не маєте доступу до цього поліса"}, status=status.HTTP_403_FORBIDDEN)
        serializer = InsurancePolicySerializer(policy)
        return Response(serializer.data)

    def delete(self, request, id):
        """Видалення конкретного поліса"""
        policy = get_object_or_404(InsurancePolicy, id=id)
        if not request.user.is_agent and policy.client != request.user:
            return Response({"error": "Ви не маєте доступу до цього поліса"}, status=status.HTTP_403_FORBIDDEN)
        policy.delete()
        return Response({"message": "Поліс успішно видалено"}, status=status.HTTP_204_NO_CONTENT)