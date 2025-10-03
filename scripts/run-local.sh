#!/bin/bash
set -e

echo "=== Starting Personal Finance API (Development) ==="

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found. Run ./scripts/bootstrap.sh first."
    exit 1
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Please copy .env.example to .env and configure it."
    exit 1
fi

# Run Django checks
echo "Running Django checks..."
python manage.py check

# Start development server
echo "Starting development server on http://127.0.0.1:8000"
python manage.py runserver
