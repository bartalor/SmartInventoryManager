from django.db import models
from .product import Product
from .warehouse import Warehouse


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    reorder_level = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in {self.warehouse.warehouse_name}"
