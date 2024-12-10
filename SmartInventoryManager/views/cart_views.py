from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from SmartInventoryManager.models import Cart, Product, CartItem
from SmartInventoryManager.serializers import CartSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


class CartView(APIView):
    def get(self, request: Request, customer_id):
        cart = Cart.objects.get(customer_id=customer_id)
        return Response(CartSerializer(cart).data)

    def post(self, request: Request, customer_id):
        cart, _ = Cart.objects.get_or_create(customer_id=customer_id)
        product = Product.objects.get(id=request.data.get('product_id'))

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += request.data.get('quantity', 1)
        item.save()

        return Response(CartSerializer(cart).data, status=HTTP_201_CREATED)