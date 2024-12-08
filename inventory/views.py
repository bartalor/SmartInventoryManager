from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from inventory.models import Product, Supplier, Category
from inventory.serializers import ProductSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST

@method_decorator(csrf_exempt, name="dispatch")
class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data})

    def post(self, request: Request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({"message": "Product created successfully", "id": product.id})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)