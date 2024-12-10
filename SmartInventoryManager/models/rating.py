from django.db import models
from .product import Product


class Rating(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="rating")
    average_score = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    total_reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name}: {self.average_score} ({self.total_reviews} reviews)"