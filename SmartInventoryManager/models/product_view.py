from django.db import models
from .product import Product
from .customer import Customer


class ProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="views")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="views")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} viewed {self.product.name} at {self.timestamp}"