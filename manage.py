#!/home/bar/myvirt/bin/python

import os
import sys
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    import SmartInventoryManager.settings
    
    # Set DJANGO_SETTINGS_MODULE as usual
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SmartInventoryManager.settings")
    
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
