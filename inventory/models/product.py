from django.db import models
from django.core.exceptions import ValidationError
import inventory.validators as vld
from inventory.models import Category, Supplier

def validate_price(value):
    if value < 0:
        raise ValidationError("Price cannot be negative.")

def validate_quantity(value):
    if value < 0:
        raise ValidationError("Quantity cannot be negative.")
    
class Product(models.Model):
                
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(null=False, blank=False, validators=[validate_quantity])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price])
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



    def __str__(self):
        return self.name