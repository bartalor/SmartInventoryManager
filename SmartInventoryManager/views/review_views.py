from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from SmartInventoryManager.models import Review, Product, Customer
from SmartInventoryManager.serializers.review_serializer import ReviewSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


class ReviewView(APIView):
    def post(self, request: Request):
        data = request.data
        customer = Customer.objects.get(id=data.get('customer_id'))
        product = Product.objects.get(id=data.get('product_id'))

        review = Review.objects.create(
            customer=customer,
            product=product,
            content=data.get('content')
        )
        return Response(ReviewSerializer(review).data, status=HTTP_201_CREATED)
