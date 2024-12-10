from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from SmartInventoryManager.models import Order, OrderDetail, Product, Customer
from SmartInventoryManager.serializers.order_serializer import OrderSerializer

class OrderView(APIView):
    def get(self, request: Request) -> Response:
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        customer_id = request.data.get('customer_id')
        items = request.data.get('items', [])

        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return Response({"error": "Invalid customer ID"}, status=HTTP_400_BAD_REQUEST)

        order = Order.objects.create(customer=customer)

        for item in items:
            try:
                product = Product.objects.get(id=item['product_id'])
            except Product.DoesNotExist:
                return Response({"error": f"Invalid product ID: {item['product_id']}"}, status=HTTP_400_BAD_REQUEST)

            quantity = item.get('quantity', 0)
            if product.quantity < quantity:
                return Response(
                    {"error": f"Not enough stock for {product.name}. Available: {product.quantity}."},
                    status=HTTP_400_BAD_REQUEST,
                )

            product.quantity -= quantity
            product.save()
            OrderDetail.objects.create(order=order, product=product, quantity=quantity, price=product.price)

        return Response(OrderSerializer(order).data, status=HTTP_201_CREATED)
