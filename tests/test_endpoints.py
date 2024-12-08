from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from inventory.models import Supplier, Category, Product

class ProductEndpointTest(APITestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(name="Endpoint Supplier", contact_info="endpoint@supplier.com")
        self.category = Category.objects.create(name="Endpoint Category")
        self.product = Product.objects.create(
            name="Existing Product",
            quantity=5,
            price=20.00,
            supplier=self.supplier,
            category=self.category
        )

    def test_get_products(self):
        url = reverse("products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["products"]), 1)
        self.assertEqual(response.data["products"][0]["name"], "Existing Product")

    def test_create_and_get_product(self):
        # Create a new product
        url = reverse("products")
        data = {
            "name": "New Endpoint Product",
            "quantity": 15,
            "price": 99.99,
            "supplier": self.supplier.id,
            "category": self.category.id,
        }
        post_response = self.client.post(url, data, format="json")
        self.assertEqual(post_response.status_code, status.HTTP_200_OK)
        self.assertEqual(post_response.data["message"], "Product created successfully")

        # Verify it exists in the database
        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(get_response.data["products"]), 2)
        self.assertEqual(get_response.data["products"][1]["name"], "New Endpoint Product")