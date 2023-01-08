from django.db import models
from customers.models import Customer
from products.models import Product
from decimal import Decimal
import random
# Create your models here.
class Order(models.Model):
    STATUS=(
        ('green','Delivred'),
        ('red','Canceled'),
        ('yellow','Wait for confirmation'),  
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    state = models.CharField(max_length=50,choices=STATUS,default='yellow')
    date_placed = models.DateTimeField(auto_now_add=True)
    date_fulfilled = models.DateTimeField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def calculate_price(self):
        qt = self.quantity
        pr = self.product.price
        self.price = Decimal(qt)* Decimal(pr)
        return self.price
 
    def __str__(self):
        return self.customer.name
    
