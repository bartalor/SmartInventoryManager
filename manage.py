#!/home/bar/myvirt/bin/python

import os
import sys

if __name__ == "__main__":
    try:
        import SmartInventoryManager.settings
    except ModuleNotFoundError as e:
        print("ModuleNotFoundError:", e)
    
    # Set DJANGO_SETTINGS_MODULE as usual
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SmartInventoryManager.settings")
    
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
