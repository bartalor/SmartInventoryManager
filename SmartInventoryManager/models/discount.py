from django.db import models
from .product import Product


class Discount(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    products = models.ManyToManyField(Product, related_name="discounts")

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"