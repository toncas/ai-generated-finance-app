"""
Pytest configuration and fixtures
"""
import pytest
from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup():
    """
    Override database setup for tests
    """
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }


@pytest.fixture
def api_client():
    """
    API client for testing
    """
    from rest_framework.test import APIClient
    return APIClient()
