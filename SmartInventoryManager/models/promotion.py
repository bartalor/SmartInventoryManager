from django.db import models
from .category import Category
from .product import Product


class Promotion(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    products = models.ManyToManyField(Product, related_name="promotions", blank=True)
    categories = models.ManyToManyField(Category, related_name="promotions", blank=True)

    def __str__(self):
        return self.name