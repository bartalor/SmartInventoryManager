from django.contrib import admin
from .models import Product, Customer, Transaction, Order
from django.db.models import Model


# Utility function to dynamically set list_display
def _get_fields(model: Model):
    return [field.name for field in model._meta.fields]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = _get_fields(Product)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = _get_fields(Customer)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = _get_fields(Transaction)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = _get_fields(Order)
