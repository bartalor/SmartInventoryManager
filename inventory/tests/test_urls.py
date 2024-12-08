from django.test import SimpleTestCase
from django.urls import resolve, reverse
from inventory.views import ProductView

class TestUrls(SimpleTestCase):

    def test_products_url_resolves(self):
        url = reverse("products")  # Ensure this matches the name in your `urls.py`
        self.assertEqual(resolve(url).func.view_class, ProductView)