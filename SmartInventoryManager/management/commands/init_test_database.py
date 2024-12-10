from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from pathlib import Path
import os


class Command(BaseCommand):
    help = "Recreate the test database and seed it with data from a fixture file"

    def add_arguments(self, parser):
        parser.add_argument(
            "file_path",
            type=str,
            help="The path to the fixture file to load",
        )

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        fixture_path = Path(file_path)

        if not fixture_path.is_file():
            self.stderr.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        test_db_config = settings.DATABASES.get("test")
        if not test_db_config:
            self.stderr.write(self.style.ERROR("No test database configured in settings!"))
            return

        test_db_name = test_db_config.get("NAME")
        if not test_db_name:
            self.stderr.write(self.style.ERROR("Test database name is not defined!"))
            return

        self.stdout.write(f"Using test database: {test_db_name}")

        if settings.DATABASES["test"]["ENGINE"] == "django.db.backends.sqlite3":
            if os.path.exists(test_db_name):
                self.stdout.write(f"Deleting test database: {test_db_name}")
                os.remove(test_db_name)
        else:
            self.stderr.write(self.style.ERROR("Test database reset only implemented for SQLite!"))
            return

        self.stdout.write("Creating a new test database...")
        try:
            call_command("migrate", "--noinput", database="test")
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error creating test database: {e}"))
            return

        try:
            call_command("loaddata", file_path, database="test")
            self.stdout.write(self.style.SUCCESS(f"Database seeded successfully with fixture: {file_path}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error seeding database: {e}"))
