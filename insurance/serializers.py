from rest_framework import serializers
from .models import User, InsurancePolicy

# Схема серіалізації для користувача
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_customer', 'is_agent', 'phone_number', 'address']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class InsurancePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurancePolicy
        fields = '__all__'
        extra_kwargs = {
            'client': {'read_only': True}  #зробити поле клієнта лише для читання
        }
