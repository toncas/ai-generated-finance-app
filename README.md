# Personal Finance Tracker API

A comprehensive REST API for personal finance management built with Django 4.2 and MongoDB.

## Features

- User authentication with JWT
- Transaction management (one-time and recurring)
- Category organization
- Budget tracking with alerts
- Financial goals monitoring
- Analytics and reporting
- Data import/export

## Technology Stack

- **Backend**: Django 4.2 LTS + Django REST Framework
- **Database**: MongoDB 6.0+ (via Djongo)
- **Cache**: Redis
- **Task Queue**: Celery + Redis
- **Authentication**: JWT (djangorestframework-simplejwt)
- **API Documentation**: drf-yasg (Swagger/OpenAPI)

## Prerequisites

- Python 3.11+
- MongoDB 6.0+
- Redis 5.0+
- pip and virtualenv

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/toncas/ai-generated-finance-app.git
cd ai-generated-finance-app
```

### 2. Bootstrap the project

```bash
./scripts/bootstrap.sh
```

This script will:
- Create a Python virtual environment
- Install all dependencies
- Create a `.env` file from `.env.example`

### 3. Configure environment variables

Edit `.env` with your configuration:

```bash
# Update these values
SECRET_KEY=your-secret-key-here
MONGO_HOST=localhost
MONGO_PORT=27017
REDIS_URL=redis://localhost:6379/1
```

### 4. Start MongoDB and Redis

```bash
# MongoDB
docker run -d -p 27017:27017 --name mongodb mongo:6.0

# Redis
docker run -d -p 6379:6379 --name redis redis:7-alpine
```

### 5. Activate virtual environment

```bash
source venv/bin/activate
```

### 6. Run Django checks

```bash
python manage.py check
```

### 7. Start the development server

```bash
python manage.py runserver
```

The API will be available at http://127.0.0.1:8000

### 8. Access API documentation

- Swagger UI: http://127.0.0.1:8000/api/docs/
- ReDoc: http://127.0.0.1:8000/api/redoc/
- Health Check: http://127.0.0.1:8000/health/

## Development Commands

Using Make:

```bash
make setup    # Bootstrap project
make run      # Run development server
make test     # Run tests
make lint     # Run linters
make format   # Format code
make clean    # Clean build artifacts
```

Or directly:

```bash
# Run development server
./scripts/run-local.sh

# Run tests
pytest

# Run linters
flake8 .
black --check .
isort --check-only .

# Format code
black .
isort .
```

## Project Structure

```
.
├── config/              # Django configuration
│   ├── settings/       # Split settings (base, dev, prod, test)
│   ├── urls.py        # URL routing
│   ├── wsgi.py        # WSGI config
│   ├── asgi.py        # ASGI config
│   └── celery.py      # Celery configuration
├── apps/               # Django applications
│   ├── users/         # User management (to be created)
│   ├── transactions/  # Transaction handling (to be created)
│   ├── categories/    # Category management (to be created)
│   ├── budgets/       # Budget tracking (to be created)
│   ├── goals/         # Financial goals (to be created)
│   └── analytics/     # Analytics & reporting (to be created)
├── core/              # Core utilities and helpers
│   ├── views.py       # Health check endpoint
│   └── urls.py        # Core URLs
├── scripts/           # Utility scripts
│   ├── bootstrap.sh   # Project setup script
│   └── run-local.sh   # Development server script
├── tests/             # Test suite (to be created)
├── docs/              # Documentation
├── manage.py          # Django management script
├── requirements.txt   # Python dependencies
├── .env.example       # Environment template
└── Makefile          # Development commands
```

## Environment Variables

Key environment variables (see `.env.example` for full list):

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | *Required* |
| `DEBUG` | Debug mode | `False` |
| `MONGO_HOST` | MongoDB host | `localhost` |
| `MONGO_DB` | Database name | `finance_tracker` |
| `REDIS_URL` | Redis connection URL | `redis://localhost:6379/1` |
| `JWT_SECRET_KEY` | JWT signing key | Uses `SECRET_KEY` |

## Testing

Run tests with pytest:

```bash
# All tests
pytest

# With coverage
pytest --cov=apps --cov=core --cov-report=html

# Specific test file
pytest tests/test_transactions.py

# With verbose output
pytest -v
```

## Security Notes

- ⚠️ Never commit `.env` file or real credentials
- Generate strong `SECRET_KEY` and `JWT_SECRET_KEY` for production
- Use environment variables or secret managers for sensitive data
- Enable HTTPS in production (see `config/settings/production.py`)
- Review CORS settings before deploying

## Next Steps

1. ✅ Repository bootstrap (TASK-001) - **COMPLETED**
2. ⏳ Create Docker Compose setup (TASK-002)
3. ⏳ Implement user authentication (TASK-006)
4. ⏳ Build transaction management (TASK-007)
5. ⏳ Add CI/CD pipeline (TASK-003)

See `kanban/tasks.md` for full task list.

## Contributing

1. Create a feature branch from `main`
2. Follow code style (Black, isort, flake8)
3. Write tests for new features
4. Submit a pull request

## License

[Add your license here]

## Support

For issues and questions, please open a GitHub issue.
