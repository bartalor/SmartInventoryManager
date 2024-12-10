from rest_framework import serializers
from inventory.models import Product
from inventory.models.product import validate_price, validate_quantity

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    
    def validate_category(self, value):
        if not value:
            raise serializers.ValidationError("Category is required.")
        return value

    def validate(self, attrs: dict):
        quantity = attrs.get('quantity')
        price = attrs.get('price')
        validate_price(price)
        validate_quantity(quantity)
        if not attrs.get("category"):
            raise serializers.ValidationError("Category is required.")
        return super().validate(attrs)