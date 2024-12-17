from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)
    REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS + ['first_name', 'last_name', 'phone_number', 'address']
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)