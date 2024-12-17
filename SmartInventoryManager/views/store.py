from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from SmartInventoryManager.models import Product, Charge

def store(request: HttpRequest):
    products = Product.objects.all()
    return render(request, "store.html", {"products": products, "user": request.user})

@login_required
def purchase_product(request: HttpRequest, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    customer = getattr(request.user, "customer_profile", None)

    if not customer:
        return render(request, "store.html", {"message": "Customer profile not found!"})

    if product.quantity <= 0:
        return render(request, "store.html", {"message": f"{product.name} is out of stock!"})

    Charge.objects.create(
        customer=customer,
        amount=product.price,
        description=f"Purchase of {product.name}"
    )

    product.quantity -= 1
    product.save()

    return render(request, "store.html", {
        "message": f"Successfully purchased {product.name} for ${product.price:.2f}. Thank you!"
    })
