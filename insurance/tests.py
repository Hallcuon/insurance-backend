from django.test import TestCase
from insurance.serializers import InsurancePolicySerializer
from insurance.models import User
from datetime import date
import re

class InsurancePolicyValidationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            is_customer=True
        )

    def test_invalid_vehicle_number(self):
        data = {
            'vehicle_number': '12345',
            'insurance_type': 'basic',
            'start_date': date(2025, 1, 1),
            'end_date': date(2026, 1, 1),
            'price': '3000.00',
            'status': 'active',
            'client': self.user.id
        }
        serializer = InsurancePolicySerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('vehicle_number', serializer.errors)

    def test_invalid_date_range(self):
        data = {
            'vehicle_number': 'AA1234BB',
            'insurance_type': 'basic',
            'start_date': date(2026, 1, 1),
            'end_date': date(2025, 1, 1),
            'price': '3000.00',
            'status': 'active',
            'client': self.user.id
        }
        serializer = InsurancePolicySerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('non_field_errors', serializer.errors)

    def test_valid_policy(self):
        data = {
            'vehicle_number': 'AA1234BB',
            'insurance_type': 'basic',
            'start_date': date(2025, 1, 1),
            'end_date': date(2026, 1, 1),
            'price': '3000.00',
            'status': 'active',
            'client': self.user.id
        }
        serializer = InsurancePolicySerializer(data=data)
        self.assertTrue(serializer.is_valid())
