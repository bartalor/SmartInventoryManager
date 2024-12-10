from rest_framework import serializers
from SmartInventoryManager.models import Order, OrderDetail
from SmartInventoryManager.serializers.customer_serializer import CustomerSerializer
from SmartInventoryManager.serializers.product_serializer import ProductSerializer


class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderDetail
        fields = ['id', 'product', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    details = OrderDetailSerializer(source='details_set', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_date', 'status', 'details']
