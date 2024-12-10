from rest_framework import serializers
from SmartInventoryManager.models import Inventory
from .product_serializer import ProductSerializer
from .warehouse_serializer import WarehouseSerializer


class InventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    warehouse = WarehouseSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = ['id', 'product', 'warehouse', 'quantity', 'reorder_level']
