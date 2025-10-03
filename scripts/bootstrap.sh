#!/bin/bash
set -e

echo "=== Personal Finance API Bootstrap Script ==="
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version || { echo "Python 3 not found. Please install Python 3.11+"; exit 1; }

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Copy .env.example to .env if .env doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from .env.example..."
    cp .env.example .env
    echo "⚠️  Please update .env with your configuration before running the app"
fi

echo ""
echo "=== Bootstrap Complete ==="
echo ""
echo "Next steps:"
echo "1. Update .env with your MongoDB and Redis configuration"
echo "2. Run 'source venv/bin/activate' to activate the virtual environment"
echo "3. Run 'python manage.py check' to validate configuration"
echo "4. Run 'python manage.py runserver' to start the development server"
echo ""
