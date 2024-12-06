from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Product
import json

@method_decorator(csrf_exempt, name="dispatch")
class ProductView(View):
    def get(self, request):
        products = list(Product.objects.values())
        return JsonResponse({"products": products})

    def post(self, request):
        data = json.loads(request.body)
        product = Product.objects.create(
            name=data["name"],
            quantity=data["quantity"],
            price=data["price"],
            supplier=data.get("supplier"),
        )
        return JsonResponse({"id": product.id, "message": "Product created successfully"})