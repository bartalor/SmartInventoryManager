import uuid
from django.db import models
from .category import Category
from .supplier import Supplier
from .tag import Tag
from django.core.exceptions import ValidationError

def validate_price(value):
    if value < 0:
        raise ValidationError("Price cannot be negative.")

def validate_quantity(value):
    if value < 0:
        raise ValidationError("Quantity cannot be negative.")
    
class Product(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[validate_quantity])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_price])
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)

    def __str__(self):
        return f"{self.name} ({self.product_id})"