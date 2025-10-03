# Personal Finance Tracker API - Engineering Document

## 1. Technology Stack

### Core Technologies
- **Python 3.11+**: Latest stable Python version for better performance and features
- **Django 4.2 LTS**: Long-term support version for stability
- **Django Rest Framework 3.14+**: RESTful API framework
- **MongoDB 6.0+**: NoSQL database for flexible schema
- **Djongo 1.3.6+**: MongoDB connector for Django ORM
- **MongoEngine 0.27+**: Document-Object Mapper for MongoDB (alternative/supplementary to Djongo)

### Supporting Libraries
- **Authentication & Security**
  - `djangorestframework-simplejwt`: JWT authentication
  - `django-cors-headers`: CORS handling
  - `cryptography`: Field-level encryption
  - `django-ratelimit`: Rate limiting

- **Data Processing**
  - `pandas`: Data manipulation for analytics
  - `numpy`: Numerical computations
  - `python-dateutil`: Date parsing and manipulation
  - `pytz`: Timezone handling

- **Caching & Performance**
  - `django-redis`: Redis cache backend
  - `redis`: Redis client
  - `celery`: Asynchronous task queue
  - `django-celery-beat`: Periodic task scheduling

- **Development & Testing**
  - `pytest-django`: Testing framework
  - `factory-boy`: Test data generation
  - `coverage`: Code coverage
  - `black`: Code formatting
  - `flake8`: Linting
  - `python-decouple`: Environment variable management

- **API Documentation**
  - `drf-spectacular`: OpenAPI 3.0 schema generation
  - `django-silk`: Profiling and inspection

## 2. Project Structure

```
personal_finance_api/
├── .env.example
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── pytest.ini
├── README.md
│
├── config/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── testing.py
│   │   ├── staging.py
│   │   └── production.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── celery.py
│
├── apps/
│   ├── __init__.py
│   │
│   ├── authentication/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── managers.py
│   │   ├── permissions.py
│   │   ├── middleware.py
│   │   ├── tokens.py
│   │   └── tests/
│   │
│   ├── users/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── signals.py
│   │   └── tests/
│   │
│   ├── transactions/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── filters.py
│   │   ├── services.py
│   │   ├── tasks.py
│   │   └── tests/
│   │
│   ├── categories/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── fixtures/
│   │   │   └── default_categories.json
│   │   └── tests/
│   │
│   ├── budgets/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── services.py
│   │   ├── tasks.py
│   │   └── tests/
│   │
│   ├── goals/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── services.py
│   │   └── tests/
│   │
│   ├── analytics/
│   │   ├── __init__.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── services.py
│   │   ├── aggregations.py
│   │   ├── cache.py
│   │   └── tests/
│   │
│   └── data_management/
│       ├── __init__.py
│       ├── views.py
│       ├── urls.py
│       ├── services.py
│       ├── importers.py
│       ├── exporters.py
│       └── tests/
│
├── core/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── pagination.py
│   ├── permissions.py
│   ├── mixins.py
│   ├── validators.py
│   ├── middleware.py
│   ├── cache.py
│   ├── encryption.py
│   └── utils.py
│
├── scripts/
│   ├── seed_data.py
│   ├── create_indexes.py
│   └── migrate_data.py
│
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── factories.py
    ├── fixtures/
    └── integration/
```

## 3. Database Design with MongoDB

### 3.1 Connection Configuration

```python
# config/settings/base.py
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': False,
        'NAME': config('MONGO_DB_NAME', default='finance_tracker'),
        'CLIENT': {
            'host': config('MONGO_HOST', default='localhost'),
            'port': config('MONGO_PORT', default=27017, cast=int),
            'username': config('MONGO_USERNAME', default=''),
            'password': config('MONGO_PASSWORD', default=''),
            'authSource': config('MONGO_AUTH_SOURCE', default='admin'),
            'authMechanism': config('MONGO_AUTH_MECHANISM', default='SCRAM-SHA-256'),
        }
    }
}

# Alternative: MongoEngine connection
import mongoengine
mongoengine.connect(
    db=config('MONGO_DB_NAME'),
    host=config('MONGO_HOST'),
    port=config('MONGO_PORT', cast=int),
    username=config('MONGO_USERNAME'),
    password=config('MONGO_PASSWORD'),
    authentication_source=config('MONGO_AUTH_SOURCE')
)
```

### 3.2 Environment Configuration (.env file)

```bash
# .env
# MongoDB Configuration
MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_DB_NAME=finance_tracker
MONGO_USERNAME=finance_user
MONGO_PASSWORD=secure_password_here
MONGO_AUTH_SOURCE=admin
MONGO_AUTH_MECHANISM=SCRAM-SHA-256

# Django Configuration
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# JWT Configuration
JWT_SECRET_KEY=your-jwt-secret-key
JWT_ACCESS_TOKEN_LIFETIME=60  # minutes
JWT_REFRESH_TOKEN_LIFETIME=7  # days

# Celery Configuration
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

### 3.3 MongoDB Collections & Indexes

```python
# scripts/create_indexes.py
from pymongo import MongoClient, ASCENDING, DESCENDING, TEXT
from django.conf import settings

def create_indexes():
    client = MongoClient(settings.DATABASES['default']['CLIENT'])
    db = client[settings.DATABASES['default']['NAME']]
    
    # Users collection
    db.users.create_index([("email", ASCENDING)], unique=True)
    db.users.create_index([("created_at", DESCENDING)])
    
    # Transactions collection
    db.transactions.create_index([("user_id", ASCENDING), ("date", DESCENDING)])
    db.transactions.create_index([("user_id", ASCENDING), ("category_id", ASCENDING)])
    db.transactions.create_index([("user_id", ASCENDING), ("type", ASCENDING)])
    db.transactions.create_index([("description", TEXT)])
    db.transactions.create_index([("tags", ASCENDING)])
    db.transactions.create_index([("created_at", DESCENDING)])
    
    # Categories collection
    db.categories.create_index([("user_id", ASCENDING), ("name", ASCENDING)], unique=True)
    db.categories.create_index([("user_id", ASCENDING), ("type", ASCENDING)])
    
    # Budgets collection
    db.budgets.create_index([("user_id", ASCENDING), ("year", ASCENDING), ("month", ASCENDING)])
    db.budgets.create_index([("user_id", ASCENDING), ("category_id", ASCENDING)])
    
    # Goals collection
    db.goals.create_index([("user_id", ASCENDING), ("status", ASCENDING)])
    db.goals.create_index([("user_id", ASCENDING), ("target_date", ASCENDING)])
    
    # Recurring templates collection
    db.recurring_templates.create_index([("user_id", ASCENDING), ("next_occurrence", ASCENDING)])
    db.recurring_templates.create_index([("user_id", ASCENDING), ("is_active", ASCENDING)])
```

## 4. Model Implementation Strategy

### 4.1 Using Djongo with MongoDB

```python
# apps/transactions/models.py
from djongo import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from decimal import Decimal
import uuid

User = get_user_model()

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('check', 'Check'),
        ('other', 'Other'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    currency = models.CharField(max_length=3, default='USD')
    category = models.ForeignKey('categories.Category', on_delete=models.PROTECT)
    description = models.CharField(max_length=255)
    date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, blank=True)
    tags = models.JSONField(default=list, blank=True)  # Store as array in MongoDB
    notes = models.TextField(blank=True)
    receipt_reference = models.CharField(max_length=255, blank=True)
    is_recurring = models.BooleanField(default=False)
    recurring_template = models.ForeignKey('RecurringTemplate', null=True, blank=True, on_delete=models.SET_NULL)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete
    
    class Meta:
        db_table = 'transactions'
        ordering = ['-date', '-created_at']
        indexes = [
            models.Index(fields=['user', '-date']),
            models.Index(fields=['user', 'category']),
            models.Index(fields=['user', 'type']),
        ]
    
    def __str__(self):
        return f"{self.type}: {self.amount} - {self.description}"
```

### 4.2 Alternative: Using MongoEngine

```python
# apps/transactions/documents.py
from mongoengine import Document, EmbeddedDocument, fields
from datetime import datetime
import uuid

class Transaction(Document):
    id = fields.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = fields.UUIDField(required=True)
    type = fields.StringField(choices=['income', 'expense'], required=True)
    amount = fields.DecimalField(min_value=0, precision=2, required=True)
    currency = fields.StringField(max_length=3, default='USD')
    category_id = fields.UUIDField(required=True)
    description = fields.StringField(max_length=255, required=True)
    date = fields.DateField(required=True)
    payment_method = fields.StringField(choices=['cash', 'credit_card', 'debit_card', 'bank_transfer', 'check', 'other'])
    tags = fields.ListField(fields.StringField(max_length=50))
    notes = fields.StringField()
    receipt_reference = fields.StringField(max_length=255)
    is_recurring = fields.BooleanField(default=False)
    recurring_template_id = fields.UUIDField()
    
    # Metadata
    created_at = fields.DateTimeField(default=datetime.utcnow)
    updated_at = fields.DateTimeField(default=datetime.utcnow)
    deleted_at = fields.DateTimeField()
    
    meta = {
        'collection': 'transactions',
        'indexes': [
            ('user_id', '-date'),
            ('user_id', 'category_id'),
            ('user_id', 'type'),
            {'fields': ['description'], 'default_language': 'english'}
        ]
    }
```

## 5. API Implementation

### 5.1 ViewSets and Serializers

```python
# apps/transactions/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Transaction
from .serializers import TransactionSerializer, TransactionCreateSerializer
from .filters import TransactionFilter
from .services import TransactionService
from core.pagination import StandardResultsSetPagination

class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = TransactionFilter
    search_fields = ['description', 'notes']
    ordering_fields = ['date', 'amount', 'created_at']
    ordering = ['-date', '-created_at']
    pagination_class = StandardResultsSetPagination
    
    def get_queryset(self):
        return Transaction.objects.filter(
            user=self.request.user,
            deleted_at__isnull=True
        ).select_related('category').prefetch_related('tags')
    
    def get_serializer_class(self):
        if self.action == 'create':
            return TransactionCreateSerializer
        elif self.action == 'bulk_create':
            return TransactionBulkCreateSerializer
        return TransactionSerializer
    
    def perform_create(self, serializer):
        transaction = serializer.save(user=self.request.user)
        # Update budget spending asynchronously
        TransactionService.update_budget_spending.delay(transaction.id)
    
    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        results = TransactionService.bulk_create_transactions(
            request.user,
            serializer.validated_data['transactions']
        )
        return Response(results, status=status.HTTP_201_CREATED)
```

### 5.2 Service Layer Pattern

```python
# apps/transactions/services.py
from celery import shared_task
from django.db import transaction
from django.core.cache import cache
from .models import Transaction
from apps.budgets.models import Budget, BudgetAlert

class TransactionService:
    
    @staticmethod
    def create_transaction(user, validated_data):
        with transaction.atomic():
            trans = Transaction.objects.create(user=user, **validated_data)
            TransactionService._invalidate_cache(user.id)
            TransactionService._check_budget_impact(trans)
            return trans
    
    @staticmethod
    @shared_task
    def update_budget_spending(transaction_id):
        try:
            trans = Transaction.objects.get(id=transaction_id)
            if trans.type == 'expense':
                budget = Budget.objects.filter(
                    user=trans.user,
                    year=trans.date.year,
                    month=trans.date.month,
                    category=trans.category
                ).first()
                
                if budget:
                    spending = Transaction.objects.filter(
                        user=trans.user,
                        type='expense',
                        category=trans.category,
                        date__year=trans.date.year,
                        date__month=trans.date.month,
                        deleted_at__isnull=True
                    ).aggregate(total=Sum('amount'))['total'] or 0
                    
                    budget.current_spending = spending
                    budget.save()
                    
                    # Check for alerts
                    if spending >= budget.amount * (budget.alert_percentage / 100):
                        BudgetAlert.objects.get_or_create(
                            budget=budget,
                            alert_type='threshold_exceeded',
                            defaults={'percentage': (spending / budget.amount) * 100}
                        )
        except Transaction.DoesNotExist:
            pass
    
    @staticmethod
    def _invalidate_cache(user_id):
        cache_keys = [
            f'user_{user_id}_transactions_*',
            f'user_{user_id}_analytics_*',
            f'user_{user_id}_summary_*',
        ]
        for pattern in cache_keys:
            cache.delete_pattern(pattern)
```

## 6. Authentication Implementation

```python
# apps/authentication/views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, LoginSerializer
from apps.users.models import User
from apps.categories.services import CategoryService

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        
        # Create default categories for new user
        CategoryService.create_default_categories(user)
        
        # Generate tokens
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'user': UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        
        if user:
            refresh = RefreshToken.for_user(user)
            
            # Log authentication event
            AuthenticationLog.objects.create(
                user=user,
                ip_address=request.META.get('REMOTE_ADDR'),
                user_agent=request.META.get('HTTP_USER_AGENT', '')
            )
            
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'user': UserSerializer(user).data
            })
        
        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

## 7. Celery Tasks for Background Processing

```python
# apps/transactions/tasks.py
from celery import shared_task
from datetime import datetime, timedelta
from .models import RecurringTemplate, Transaction

@shared_task
def process_recurring_transactions():
    """Process all due recurring transactions"""
    today = datetime.now().date()
    templates = RecurringTemplate.objects.filter(
        is_active=True,
        next_occurrence__lte=today
    )
    
    for template in templates:
        # Create transaction from template
        transaction = Transaction.objects.create(
            user=template.user,
            type=template.type,
            amount=template.amount,
            category=template.category,
            description=template.description,
            date=template.next_occurrence,
            payment_method=template.payment_method,
            is_recurring=True,
            recurring_template=template
        )
        
        # Calculate next occurrence
        template.calculate_next_occurrence()
        template.save()
        
        # Send notification
        send_recurring_transaction_notification.delay(
            template.user.id,
            transaction.id
        )

# config/celery.py
from celery import Celery
from celery.schedules import crontab

app = Celery('personal_finance')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'process-recurring-transactions': {
        'task': 'apps.transactions.tasks.process_recurring_transactions',
        'schedule': crontab(hour=0, minute=0),  # Run daily at midnight
    },
    'generate-budget-alerts': {
        'task': 'apps.budgets.tasks.generate_budget_alerts',
        'schedule': crontab(hour=9, minute=0),  # Run daily at 9 AM
    },
}
```

## 8. Caching Strategy

```python
# config/settings/base.py
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('REDIS_URL', default='redis://127.0.0.1:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            },
            'MAX_CONNECTIONS': 1000,
            'PICKLE_VERSION': -1,
        },
        'KEY_PREFIX': 'finance_tracker',
        'TIMEOUT': 300,  # 5 minutes default
    }
}

# apps/analytics/cache.py
from django.core.cache import cache
from functools import wraps
import hashlib
import json

def cache_result(timeout=300, key_prefix=''):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate cache key
            cache_key = f"{key_prefix}:{func.__name__}"
            if args:
                # Include user_id if present
                if hasattr(args[0], 'user'):
                    cache_key += f":user_{args[0].user.id}"
            
            # Include kwargs in cache key
            if kwargs:
                kwargs_str = json.dumps(kwargs, sort_keys=True)
                kwargs_hash = hashlib.md5(kwargs_str.encode()).hexdigest()
                cache_key += f":{kwargs_hash}"
            
            # Try to get from cache
            result = cache.get(cache_key)
            if result is not None:
                return result
            
            # Calculate and cache result
            result = func(*args, **kwargs)
            cache.set(cache_key, result, timeout)
            return result
        
        return wrapper
    return decorator
```

## 9. Testing Strategy

```python
# tests/conftest.py
import pytest
from rest_framework.test import APIClient
from apps.users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticated_client(api_client, test_user):
    refresh = RefreshToken.for_user(test_user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return api_client

@pytest.fixture
def test_user(db):
    return User.objects.create_user(
        email='test@example.com',
        password='testpass123',
        first_name='Test',
        last_name='User'
    )

# apps/transactions/tests/test_views.py
import pytest
from decimal import Decimal
from datetime import date
from apps.transactions.models import Transaction
from apps.categories.models import Category

@pytest.mark.django_db
class TestTransactionAPI:
    
    def test_create_transaction(self, authenticated_client, test_user):
        category = Category.objects.create(
            user=test_user,
            name='Groceries',
            type='expense'
        )
        
        data = {
            'type': 'expense',
            'amount': '50.00',
            'category_id': str(category.id),
            'description': 'Weekly groceries',
            'date': date.today().isoformat()
        }
        
        response = authenticated_client.post('/api/v1/transactions/', data)
        
        assert response.status_code == 201
        assert response.data['amount'] == '50.00'
        assert Transaction.objects.count() == 1
    
    def test_list_transactions_with_pagination(self, authenticated_client, test_user):
        # Create 25 transactions
        category = Category.objects.create(user=test_user, name='Test', type='expense')
        for i in range(25):
            Transaction.objects.create(
                user=test_user,
                type='expense',
                amount=Decimal('10.00'),
                category=category,
                description=f'Transaction {i}',
                date=date.today()
            )
        
        response = authenticated_client.get('/api/v1/transactions/')
        
        assert response.status_code == 200
        assert response.data['count'] == 25
        assert len(response.data['results']) == 20  # Default page size
        assert response.data['next'] is not None
```

## 10. Deployment Configuration

### 10.1 Docker Setup

```dockerfile
# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
```

### 10.2 Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - mongodb
      - redis

  mongodb:
    image: mongo:6.0
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: ${MONGO_USERNAME}
      MONGO_INITDB_ROOT_PASSWORD: ${MONGO_PASSWORD}
      MONGO_INITDB_DATABASE: ${MONGO_DB_NAME}
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"

  celery:
    build: .
    command: celery -A config worker -l info
    volumes:
      - .:/app
    env_file:
      - .env
    depends_on:
      - mongodb
      - redis

  celery-beat:
    build: .
    command: celery -A config beat -l info
    volumes:
      - .:/app
    env_file:
      - .env
    depends_on:
      - mongodb
      - redis

volumes:
  mongo_data:
```

## 11. Performance Optimization

### 11.1 Database Query Optimization
- Use MongoDB aggregation pipelines for complex queries
- Implement proper indexing strategy
- Use projection to limit returned fields
- Implement cursor-based pagination for large datasets

### 11.2 Caching Strategy
- Cache frequently accessed data (categories, budgets)
- Implement cache warming for analytics
- Use cache tags for efficient invalidation
- Redis for session storage

### 11.3 API Response Optimization
- Implement field filtering
- Use compression middleware
- Implement response pagination
- Lazy loading for related objects

## 12. Security Implementation

### 12.1 Field Encryption
```python
# core/encryption.py
from cryptography.fernet import Fernet
from django.conf import settings

class FieldEncryption:
    def __init__(self):
        self.cipher = Fernet(settings.ENCRYPTION_KEY.encode())
    
    def encrypt(self, value):
        if value is None:
            return None
        return self.cipher.encrypt(str(value).encode()).decode()
    
    def decrypt(self, value):
        if value is None:
            return None
        return self.cipher.decrypt(value.encode()).decode()
```

### 12.2 Rate Limiting
```python
# core/middleware.py
from django.core.cache import cache
from rest_framework.exceptions import Throttled

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.user.is_authenticated:
            key = f"rate_limit:{request.user.id}"
            requests = cache.get(key, 0)
            
            if requests >= 1000:  # 1000 requests per hour
                raise Throttled(detail="Rate limit exceeded")
            
            cache.set(key, requests + 1, 3600)  # 1 hour TTL
        
        response = self.get_response(request)
        return response
```

## 13. Monitoring and Logging

```python
# config/settings/production.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/finance_tracker/app.log',
            'maxBytes': 1024 * 1024 * 15,  # 15MB
            'backupCount': 10,
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'INFO',
    },
}
```

## 14. Development Workflow

### 14.1 Git Workflow
- Main branch for production
- Develop branch for integration
- Feature branches for new features
- Hotfix branches for urgent fixes

### 14.2 Code Quality
- Pre-commit hooks for linting
- Automated testing in CI/CD
- Code review requirements
- Documentation standards

### 14.3 CI/CD Pipeline
- GitHub Actions for CI
- Automated testing on PR
- Docker image building
- Deployment to staging/production