from rest_framework import serializers
from SmartInventoryManager.models import ProductView


class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductView
        fields = ['id', 'product', 'customer', 'timestamp']