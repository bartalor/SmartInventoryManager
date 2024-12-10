from django.test import TestCase
from SmartInventoryManager.models import Product, Customer, Transaction
from SmartInventoryManager.models import Category, Supplier
class TransactionModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.supplier = Supplier.objects.create(name="Test Supplier")
        self.product = Product.objects.create(name="Test Product", quantity=100, price=10.99, category=self.category, supplier=self.supplier)
        self.customer = Customer.objects.create(name="Test Customer", contact_info="test@example.com")

    def test_transaction_creation(self):
        transaction = Transaction.objects.create(
            transaction_type="sale",
            product=self.product,
            customer=self.customer,
            quantity=5
        )
        self.assertEqual(transaction.quantity, 5)
        self.assertEqual(transaction.transaction_type, "sale")
