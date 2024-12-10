from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from SmartInventoryManager.models import ProductView, Product, Customer
from SmartInventoryManager.serializers.product_view_serializer import ProductViewSerializer
from rest_framework.status import HTTP_201_CREATED


class ProductViewLogView(APIView):
    def post(self, request: Request):
        data = request.data
        product = Product.objects.get(id=data.get('product_id'))
        customer = Customer.objects.get(id=data.get('customer_id'))

        view = ProductView.objects.create(product=product, customer=customer)
        return Response(ProductViewSerializer(view).data, status=HTTP_201_CREATED)