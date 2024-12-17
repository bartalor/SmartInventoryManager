from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from SmartInventoryManager.models import Product, InventoryProduct

def store(request: HttpRequest):
    products = Product.objects.all()
    return render(request, "store.html", {"products": products, "user": request.user})

@login_required
def purchase_product(request: HttpRequest, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    inventory_product = get_object_or_404(InventoryProduct, product=product)
    customer = getattr(request.user, "customer_profile", None)

    if not customer:
        return render(request, "store.html", {"message": "Customer profile not found!"})

    if inventory_product.quantity <= 0:
        return render(request, "store.html", {"message": f"{product.name} is out of stock!"})


    inventory_product.quantity -= 1
    inventory_product.save()

    return render(request, "store.html", {
        "message": f"Successfully purchased {product.name} for ${product.price:.2f}. Thank you!"
    })
