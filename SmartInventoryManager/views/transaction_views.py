from rest_framework.views import APIView
from rest_framework.response import Response
from SmartInventoryManager.models import Transaction
from SmartInventoryManager.serializers import TransactionSerializer

class TransactionView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response({'transactions': serializer.data})