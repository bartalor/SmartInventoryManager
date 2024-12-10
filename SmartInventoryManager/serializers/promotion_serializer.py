from rest_framework import serializers
from SmartInventoryManager.models import Promotion
from .product_serializer import ProductSerializer
from .category_serializer import CategorySerializer


class PromotionSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Promotion
        fields = ['id', 'name', 'start_date', 'end_date', 'products', 'categories']