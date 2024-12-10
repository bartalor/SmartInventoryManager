from django.core.management.base import BaseCommand
from SmartInventoryManager.models import Category, Product, Tag


class Command(BaseCommand):
    help = "Inspect relationships between Categories, Tags, and Products"

    def handle(self, *args, **kwargs) -> None:
        self.stdout.write("Inspecting Categories and Tags...\n")

        # Fetch all categories
        categories = Category.objects.all()
        for category in categories:
            self.stdout.write(f"Category: {category.name}")
            products = Product.objects.filter(category=category)
            for product in products:
                self.stdout.write(f"  Product: {product.name}")
                tags = product.tags.all()
                if tags.exists():
                    self.stdout.write(f"    Tags: {[tag.name for tag in tags]}")
                else:
                    self.stdout.write("    Tags: None")

        self.stdout.write("\nInspection complete.")