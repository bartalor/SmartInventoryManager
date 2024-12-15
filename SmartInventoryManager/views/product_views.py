from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from SmartInventoryManager.models import Product
from SmartInventoryManager.serializers import ProductSerializer
from django.db.models import Q

class ProductView(APIView):
    def get(self, request: Request):
        queryset = Product.objects.all()

        category = request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name__icontains=category)

        tags = request.query_params.getlist('tags')
        if tags:
            queryset = queryset.filter(tags__name__in=tags).distinct()

        price_min = request.query_params.get('price_min')
        price_max = request.query_params.get('price_max')
        if price_min:
            queryset = queryset.filter(price__gte=float(price_min))
        if price_max:
            queryset = queryset.filter(price__lte=float(price_max))

        supplier = request.query_params.get('supplier')
        if supplier:
            queryset = queryset.filter(supplier__name__icontains=supplier)

        serializer = ProductSerializer(queryset, many=True)
        return Response({'products': serializer.data})
