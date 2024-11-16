# wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LinkedIn.settings')  # Replace with your project's settings

application = get_wsgi_application()
