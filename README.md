# Personal Finance Tracker API

A comprehensive REST API for personal finance management built with Django REST Framework and MongoDB.

## Technology Stack

- **Python 3.11+**
- **Django 4.2 LTS**
- **Django REST Framework 3.14+**
- **MongoDB 6.0+** with Djongo
- **Redis** for caching
- **Celery** for async tasks
- **JWT** for authentication

## Quick Start

### Prerequisites

- Python 3.11+
- MongoDB 6.0+
- Redis 6.0+
- Docker and Docker Compose (optional)

### Setup Instructions

#### Option 1: Using Docker Compose (Recommended)

1. Clone the repository and navigate to the project root
2. Copy the environment template:
   ```bash
   cp .env.example .env
   ```
3. Update `.env` with your configuration
4. Build and run the containers:
   ```bash
   docker-compose up --build
   ```
5. In a new terminal, run migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   ```
6. Create indexes:
   ```bash
   docker-compose exec web python scripts/create_indexes.py
   ```
7. Create a superuser (optional):
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```
8. The API will be available at `http://localhost:8000`

#### Option 2: Local Setup

1. Clone the repository and navigate to the project root
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy the environment template:
   ```bash
   cp .env.example .env
   ```
5. Update `.env` with your configuration (ensure MongoDB and Redis are running)
6. Run migrations:
   ```bash
   python manage.py migrate
   ```
7. Create indexes:
   ```bash
   python scripts/create_indexes.py
   ```
8. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```
9. Run the development server:
   ```bash
   python manage.py runserver
   ```
10. The API will be available at `http://localhost:8000`

### Running Tests

```bash
# Using Docker
docker-compose exec web pytest

# Local setup
pytest
```

### API Documentation

- OpenAPI/Swagger UI: `http://localhost:8000/api/schema/swagger-ui/`
- ReDoc: `http://localhost:8000/api/schema/redoc/`
- OpenAPI Schema: `http://localhost:8000/api/schema/`

## Project Structure

```
personal_finance_api/
├── config/             # Django project configuration
├── apps/               # Django applications
│   ├── authentication/ # JWT auth and user management
│   ├── transactions/   # Transaction management
│   ├── categories/     # Category management
│   ├── budgets/        # Budget tracking
│   ├── goals/          # Financial goals
│   └── analytics/      # Analytics and reporting
├── core/               # Shared utilities and base classes
├── scripts/            # Management scripts
└── tests/              # Test suite
```

## Environment Variables

See `.env.example` for all available configuration options. Key variables:

- `SECRET_KEY`: Django secret key (generate a new one for production)
- `DEBUG`: Set to False in production
- `MONGO_*`: MongoDB connection settings
- `REDIS_URL`: Redis connection URL
- `JWT_SECRET_KEY`: Secret key for JWT signing

## Available Endpoints

See the OpenAPI documentation for complete endpoint details. Main endpoints:

- `/api/auth/` - Authentication (register, login, refresh, logout)
- `/api/transactions/` - Transaction CRUD and filtering
- `/api/categories/` - Category management
- `/api/budgets/` - Budget creation and tracking
- `/api/goals/` - Financial goal management
- `/api/analytics/` - Analytics and reporting

## Development

### Code Style

- Follow PEP 8
- Use Black for formatting: `black .`
- Use flake8 for linting: `flake8`

### Contributing

1. Create a feature branch from `main`
2. Make your changes with tests
3. Ensure all tests pass
4. Submit a pull request

## Security

- Never commit `.env` files or secrets
- Use strong `SECRET_KEY` and `JWT_SECRET_KEY` values
- Enable HTTPS in production
- Keep dependencies updated
- Follow Django security best practices

## License

See LICENSE file for details.
