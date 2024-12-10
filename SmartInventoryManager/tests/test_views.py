from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from inventory.models import Supplier, Category

class ProductAPIViewTest(APITestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(name="Supplier A", contact_info="contact@suppliera.com")
        self.category = Category.objects.create(name="Category A")

    def test_get_empty_products(self):
        url = reverse("products")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["products"]), 0)

    def test_create_product(self):
        url = reverse("products")
        data = {
            "name": "New Product",
            "quantity": 5,
            "price": 49.99,
            "supplier": self.supplier.id,
            "category": self.category.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Product created successfully")

    def test_create_product_missing_fields(self):
        url = reverse("products")
        data = {
            "name": "",
            "quantity": 5,
            "price": 49.99,
            "supplier": self.supplier.id,
            # Missing category
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("category", response.data)