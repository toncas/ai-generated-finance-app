"""
URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Personal Finance Tracker API",
      default_version='v1',
      description="API for managing personal finances",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@financetracker.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API Documentation
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Health check
    path('health/', include('core.urls')),
    
    # API endpoints (to be added)
    # path('api/v1/auth/', include('apps.users.urls')),
    # path('api/v1/transactions/', include('apps.transactions.urls')),
    # path('api/v1/categories/', include('apps.categories.urls')),
    # path('api/v1/budgets/', include('apps.budgets.urls')),
    # path('api/v1/goals/', include('apps.goals.urls')),
    # path('api/v1/analytics/', include('apps.analytics.urls')),
]
