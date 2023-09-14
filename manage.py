#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Set the DJANGO_SETTINGS_MODULE environment variable to 'weather_project.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_project.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute Django commands using command-line arguments (sys.argv)
    execute_from_command_line(sys.argv)


# Entry point of the script
if __name__ == '__main__':
    main()
