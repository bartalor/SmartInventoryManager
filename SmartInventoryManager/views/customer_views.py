from rest_framework.views import APIView
from rest_framework.response import Response
from SmartInventoryManager.models import Customer
from SmartInventoryManager.serializers import CustomerSerializer

class CustomerView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({'customers': serializer.data})