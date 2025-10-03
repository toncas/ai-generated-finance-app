.PHONY: help setup install run test lint format clean

help:
	@echo "Personal Finance API - Makefile commands"
	@echo ""
	@echo "  make setup    - Bootstrap the project (create venv, install deps)"
	@echo "  make install  - Install/update dependencies"
	@echo "  make run      - Run development server"
	@echo "  make test     - Run tests"
	@echo "  make lint     - Run linters"
	@echo "  make format   - Format code"
	@echo "  make clean    - Clean build artifacts"

setup:
	./scripts/bootstrap.sh

install:
	pip install -r requirements.txt

run:
	./scripts/run-local.sh

test:
	pytest

lint:
	flake8 .
	isort --check-only .

format:
	black .
	isort .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/
