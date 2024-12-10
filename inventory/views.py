from rest_framework.views import APIView
from rest_framework.response import Response
from inventory.models import Transaction, Customer, Product
from inventory.serializers import CustomerSerializer, TransactionSerializer, ProductSerializer

class CustomerView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({'customers': serializer.data})

class TransactionView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response({'transactions': serializer.data})
    

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})