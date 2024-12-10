from rest_framework.views import APIView
from rest_framework.response import Response
from SmartInventoryManager.models import Inventory

class InventoryView(APIView):
    def get(self, request, product_id):
        inventory = Inventory.objects.filter(product_id=product_id)
        data = [{"warehouse": i.warehouse.warehouse_name, "quantity": i.quantity} for i in inventory]
        return Response({'product_id': product_id, 'stock': data})