"""
WSGI config for ecomSys_e20_02_nguyendinhtung project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomSys_e20_02_nguyendinhtung.settings')

application = get_wsgi_application()
