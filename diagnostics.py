import os
import django
import sqlite3

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory.settings')
django.setup()

# Path to the database as defined in settings.py
DB_PATH = '/home/bar/data/SmartInventoryManager/db.sqlite3'

def check_installed_apps():
    from django.conf import settings
    print("=== Step 1: Check INSTALLED_APPS ===")
    if 'inventory' in settings.INSTALLED_APPS:
        print("SUCCESS: 'inventory' is in INSTALLED_APPS")
    else:
        print("FAILURE: 'inventory' is NOT in INSTALLED_APPS")
    print()

def check_model_definition():
    try:
        from inventory.models import Product
        print("=== Step 2: Check Product Model Definition ===")
        print("SUCCESS: Product model imported successfully")
        print("Fields:", [field.name for field in Product._meta.fields])
    except Exception as e:
        print("FAILURE: Error importing Product model:", e)
    print()

def check_migrations():
    from django.db.migrations.executor import MigrationExecutor
    from django.db import connections
    print("=== Step 3: Check Migrations ===")
    connection = connections['default']
    executor = MigrationExecutor(connection)
    applied_migrations = executor.loader.applied_migrations
    if any('inventory' in migration for migration in applied_migrations):
        print("SUCCESS: Migrations for 'inventory' are applied")
    else:
        print("FAILURE: No applied migrations for 'inventory'")
    print()

def check_database_table_sqlite():
    print("=== Step 4: Check Database Table in SQLite ===")
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='inventory_product';")
        table = cursor.fetchone()
        if table:
            print("SUCCESS: 'inventory_product' table exists in SQLite database")
        else:
            print("FAILURE: 'inventory_product' table does NOT exist in SQLite database")
        conn.close()
    except Exception as e:
        print("FAILURE: Error while checking the database table in SQLite:", e)
    print()

def check_database_table_django_orm():
    print("=== Step 5: Check Database Table Using Django ORM ===")
    try:
        from inventory.models import Product
        if Product.objects.exists():
            print("SUCCESS: 'inventory_product' table exists and has data (verified via ORM)")
        else:
            print("SUCCESS: 'inventory_product' table exists but is empty (verified via ORM)")
    except Exception as e:
        print("FAILURE: Error while querying 'inventory_product' table via ORM:", e)
    print()

def run_diagnostics():
    print("=== Django Diagnostics Script ===")
    print()
    check_installed_apps()
    check_model_definition()
    check_migrations()
    check_database_table_sqlite()
    check_database_table_django_orm()
    print("=== Diagnostics Complete ===")

if __name__ == '__main__':
    run_diagnostics()
