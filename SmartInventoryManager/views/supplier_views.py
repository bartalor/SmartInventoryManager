from rest_framework.views import APIView
from rest_framework.response import Response
from SmartInventoryManager.models import Supplier

class SupplierView(APIView):
    def get(self, request):
        suppliers = Supplier.objects.all()
        data = [{"id": s.id, "name": s.name, "contact_email": s.contact_email} for s in suppliers]
        return Response({'suppliers': data})