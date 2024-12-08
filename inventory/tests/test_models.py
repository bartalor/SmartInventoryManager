from django.test import TestCase
from inventory.models import Supplier, Category, Product
from django.core.exceptions import ValidationError

class ProductModelTest(TestCase):

    def setUp(self):
        self.supplier = Supplier.objects.create(name="Supplier A", contact_info="suppliera@test.com")
        self.category = Category.objects.create(name="Category A")

    def test_create_product(self):
        product = Product.objects.create(
            name="Test Product",
            quantity=10,
            price=99.99,
            supplier=self.supplier,
            category=self.category,
        )
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.supplier, self.supplier)
        self.assertEqual(product.category, self.category)

    def test_invalid_price(self):
        with self.assertRaises(ValidationError):
            product = Product.objects.create(
                name="Invalid Product",
                quantity=10,
                price=-1.0,
                supplier=self.supplier,
                category=self.category,
            )
            product.full_clean()