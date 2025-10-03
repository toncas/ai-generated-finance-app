"""
Core views
"""
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def health_check(request):
    """
    Health check endpoint for load balancers and monitoring
    """
    return JsonResponse({
        'status': 'ok',
        'service': 'personal-finance-api'
    })
