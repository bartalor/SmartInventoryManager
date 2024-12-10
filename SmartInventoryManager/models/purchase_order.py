from django.db import models
from .supplier import Supplier
from .product import Product


class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    expected_delivery_date = models.DateField()

    def __str__(self):
        return f"Purchase Order {self.id} - {self.supplier.name}"