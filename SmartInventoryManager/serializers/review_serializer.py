from rest_framework import serializers
from SmartInventoryManager.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'customer', 'product', 'content', 'created_at']