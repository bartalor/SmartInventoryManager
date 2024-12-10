from rest_framework import serializers
from SmartInventoryManager.models import Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Warehouse
        fields = ['id', 'warehouse_name', 'location', 'parent']
