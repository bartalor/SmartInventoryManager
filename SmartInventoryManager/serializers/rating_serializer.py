from rest_framework import serializers
from SmartInventoryManager.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'product', 'average_score', 'total_reviews']