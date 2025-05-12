from rest_framework import serializers
from .models import User, InsurancePolicy
import re

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
            'client': {'read_only': True}
        }
    
    def validate_vehicle_number(self, value):
        pattern = r'^[А-ЯA-Z]{2}\d{4}[А-ЯA-Z]{2}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("Невірний формат номерного знаку. Має бути типу 'AA1234BB'.")
        return value
    
    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("Дата завершення має бути пізнішою за дату початку.")
        return data