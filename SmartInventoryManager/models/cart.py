from django.db import models
from .product import Product
from .customer import Customer


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="cart")
    products = models.ManyToManyField(Product, through="CartItem", related_name="carts")

    def __str__(self):
        return f"Cart for {self.customer.name}"