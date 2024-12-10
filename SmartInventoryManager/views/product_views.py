from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_400_BAD_REQUEST
from SmartInventoryManager.models import Product
from SmartInventoryManager.serializers import ProductSerializer

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})

    def post(self, request: Request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({"message": "Product created successfully", "id": product.id})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)