from django.db import models
from decimal import Decimal

# Create your models here.
class Product(models.Model):
  
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    
