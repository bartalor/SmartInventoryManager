from django.db import models
from .user import User

class Charge(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="charges")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - ${self.amount} on {self.date.strftime('%Y-%m-%d')}"
