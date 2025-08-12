from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    STATUS_CHOICES = [
        ('free', 'Свободно'),
        ('rented', 'Арендовано'),
        ('maintenance', 'На обслуживании'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='free')

    def __str__(self):
        return self.address


class Rental(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tenant_name} - {self.property.address}"
