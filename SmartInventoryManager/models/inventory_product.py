from django.db import models
from .product import Product

class InventoryProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="inventory")
    quantity = models.PositiveIntegerField(default=0)
    class Meta:
        db_table = 'inventory_product'

    def __str__(self):
        return f"{self.product.name}: {self.quantity} in stock"
