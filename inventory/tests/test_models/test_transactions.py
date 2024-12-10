from django.test import TestCase
from inventory.models import Product, Customer, Transaction

# tests/test_models.py
class TransactionModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", quantity=100, price=10.99)
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
