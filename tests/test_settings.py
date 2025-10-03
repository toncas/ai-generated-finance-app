"""
Test Django settings configuration
"""
import pytest
from django.conf import settings


class TestSettings:
    """
    Tests for Django settings
    """
    
    def test_debug_disabled_in_test(self):
        """
        Test that DEBUG is disabled in test environment
        """
        assert settings.DEBUG is False
    
    def test_database_is_sqlite_in_memory(self):
        """
        Test that test database uses SQLite in-memory
        """
        assert settings.DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3'
        assert settings.DATABASES['default']['NAME'] == ':memory:'
    
    def test_rest_framework_configured(self):
        """
        Test that REST framework is properly configured
        """
        assert 'rest_framework' in settings.INSTALLED_APPS
        assert 'DEFAULT_AUTHENTICATION_CLASSES' in settings.REST_FRAMEWORK
        assert 'DEFAULT_PERMISSION_CLASSES' in settings.REST_FRAMEWORK
    
    def test_jwt_settings_present(self):
        """
        Test that JWT settings are configured
        """
        assert hasattr(settings, 'SIMPLE_JWT')
        assert 'ACCESS_TOKEN_LIFETIME' in settings.SIMPLE_JWT
        assert 'REFRESH_TOKEN_LIFETIME' in settings.SIMPLE_JWT
