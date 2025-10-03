"""
Test health check endpoint
"""
import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestHealthCheck:
    """
    Tests for health check endpoint
    """
    
    def test_health_check_returns_200(self, api_client):
        """
        Test that health check endpoint returns 200 OK
        """
        url = reverse('health-check')
        response = api_client.get(url)
        
        assert response.status_code == 200
        assert response.json()['status'] == 'ok'
        assert response.json()['service'] == 'personal-finance-api'
    
    def test_health_check_no_auth_required(self, api_client):
        """
        Test that health check doesn't require authentication
        """
        url = reverse('health-check')
        # Don't set any authentication
        response = api_client.get(url)
        
        assert response.status_code == 200
