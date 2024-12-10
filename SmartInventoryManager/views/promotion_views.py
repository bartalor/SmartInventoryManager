from rest_framework.views import APIView
from rest_framework.response import Response
from SmartInventoryManager.models import Promotion

class PromotionView(APIView):
    def get(self, request):
        promotions = Promotion.objects.all()
        data = [{"name": p.name, "start_date": p.start_date, "end_date": p.end_date} for p in promotions]
        return Response({'promotions': data})