from django.test import TestCase
from django.urls import reverse
from SmartInventoryManager.models import Supplier, Category, Product
from rest_framework.test import APIClient

class ProductIntegrationTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create(name="Integration Supplier", contact_info="integration@supplier.com")
        self.category = Category.objects.create(name="Integration Category")

    def test_full_product_lifecycle(self):
        # 1. Create a new product
        create_url = reverse("products")
        product_data = {
            "name": "Lifecycle Product",
            "quantity": 10,
            "price": 50.0,
            "supplier": self.supplier.id,
            "category": self.category.id,
        }
        create_response = self.client.post(create_url, product_data, format="json")
        self.assertEqual(create_response.status_code, 200)
        self.assertIn("message", create_response.data)

        # 2. Verify the product exists
        get_url = reverse("products")
        get_response = self.client.get(get_url)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(len(get_response.data["products"]), 1)
        self.assertEqual(get_response.data["products"][0]["name"], "Lifecycle Product")

        # 3. Delete the product
        product_id = get_response.data["products"][0]["id"]
        delete_url = f"/products/{product_id}/"  # Assuming you have a delete endpoint
        delete_response = self.client.delete(delete_url)
        self.assertEqual(delete_response.status_code, 204)

        # 4. Verify the product no longer exists
        get_response_after_delete = self.client.get(get_url)
        self.assertEqual(len(get_response_after_delete.data["products"]), 0)