#!/usr/bin/env python
import os
import sys

# in order for this management command file to work outside of the test environment
# we need to insert that folder into the path
from sys import path
path.insert(1,"selenium_magic_test_django_project")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "selenium_magic_test_django_project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
