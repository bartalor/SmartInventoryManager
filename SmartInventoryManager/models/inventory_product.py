from django.db import models
from .product import Product

class InventoryProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="inventory")
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name}: {self.stock} in stock"
