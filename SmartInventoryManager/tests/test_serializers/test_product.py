from django.test import TestCase
from inventory.models import Supplier, Category, Product
from inventory.serializers import ProductSerializer

class ProductSerializerTest(TestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(name="Test Supplier", contact_info="supplier@test.com")
        self.category = Category.objects.create(name="Test Category")
        self.valid_data = {
            "name": "Test Product",
            "quantity": 10,
            "price": 99.99,
            "supplier": self.supplier.id,
            "category": self.category.id,
        }
        self.invalid_data = {
            "name": "",
            "quantity": -5,
            "price": -10.0,
            "supplier": None,
            "category": None,
        }

    def test_valid_data(self):
        serializer = ProductSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["name"], self.valid_data["name"])

    def test_invalid_data(self):
        serializer = ProductSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("name", serializer.errors)
        self.assertIn("quantity", serializer.errors)
        self.assertIn("price", serializer.errors)