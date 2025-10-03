"""
Development settings
"""
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Development-specific apps
INSTALLED_APPS += [
    'django_extensions',
]

# Disable HTTPS redirect in development
SECURE_SSL_REDIRECT = False

# Debug toolbar (optional)
# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
# INTERNAL_IPS = ['127.0.0.1']
