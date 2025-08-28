from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)


class MenuItem(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    price = models.DecimalField(
        max_digits = 8, decimal_places = 2,
        validators = [MinValueValidator(Decimal('0.00'))]
    )
    is_available = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Contact(models.model):
    name = models.CharField(max_length=120, blank=True, null= True)
    email = models.EmailField(blank= True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)