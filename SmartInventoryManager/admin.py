from django.contrib import admin
from .models import Product
from django.db.models import Model


# Utility function to dynamically set list_display
def _get_fields(model: Model):
    return [field.name for field in model._meta.fields]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = _get_fields(Product)
