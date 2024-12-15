from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('customer', 'Customer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    def is_admin(self):
        print(self.groups)
        return self.role == 'admin'

    def is_staff_member(self):
        return self.role == 'staff'

    def is_customer(self):
        return self.role == 'customer'
