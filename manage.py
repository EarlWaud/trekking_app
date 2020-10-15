#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import Pillow
from Pillow import Image
import request

def main():
    username = request.form['username']
    print( username )
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'panoramic_trekking_app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    #Open image using Image module
    im = Image.open("images/cuba.jpg")
    #Show actual Image
    im.show()
    #Show rotated Image
    im = im.rotate(45)
    im.show()

if __name__ == '__main__':
    main()
