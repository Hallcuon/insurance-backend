from django.db import models
from django.contrib.auth.models import AbstractUser

# Користувач (розширений User)
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username

# Страховий поліс
class InsurancePolicy(models.Model):
    POLICY_TYPES = (
        ('basic', 'Basic Coverage'),
        ('full', 'Full Coverage'),
    )

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='policies')
    vehicle_number = models.CharField(max_length=10)
    insurance_type = models.CharField(max_length=10, choices=POLICY_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"Policy {self.id} for {self.client.username}"
