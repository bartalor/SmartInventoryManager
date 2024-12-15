from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.apps import apps
from pathlib import Path


class Command(BaseCommand):
    help = "Reset specific tables (delete all rows) and seed them with data from a fixture file"

    def add_arguments(self, parser):
        parser.add_argument(
            "file_path",
            type=str,
            help="The path to the fixture file to load",
        )

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        tables = [
            'category', 'supplier', 'tag', 'product',
            'customer', 'order', 'orderdetail', 'warehouse', 'inventory'
        ]

        if not Path(file_path).is_file():
            self.stderr.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        self.stdout.write("Resetting specific tables (deleting all rows)...")
        for table_name in tables:
            try:
                model = apps.get_model('SmartInventoryManager', table_name)
                model.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(f"Reset table '{table_name}'."))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Error resetting table '{table_name}': {e}"))

        self.stdout.write("Loading fixture data...")
        try:
            call_command("loaddata", file_path)
            self.stdout.write(self.style.SUCCESS(f"Fixture data loaded successfully: {file_path}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error loading fixture: {e}"))
