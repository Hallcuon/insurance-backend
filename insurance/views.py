from django.shortcuts import render
from rest_framework import generics
from .models import User, InsurancePolicy
from .serializers import UserSerializer, InsurancePolicySerializer
from rest_framework.permissions import IsAuthenticated

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

