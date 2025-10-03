"""Development settings."""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
DATABASES['default']['CLIENT']['host'] = 'localhost'

# Additional development apps
INSTALLED_APPS += [
    'django_extensions',
]

# Development-specific middleware
MIDDLEWARE += []

# CORS - Allow all origins in development
CORS_ALLOW_ALL_ORIGINS = True

# Email - Use console backend in development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Logging - More verbose in development
LOGGING['handlers']['console']['level'] = 'DEBUG'
LOGGING['root']['level'] = 'DEBUG'
