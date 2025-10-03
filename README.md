# AI-Generated Finance App

Repository bootstrap and developer quickstart (TASK-001)

This project is a Personal Finance Tracker API. This branch implements the TASK-001 bootstrap: a minimal developer-friendly skeleton so contributors can run a local stub server and follow a reproducible quickstart.

Prerequisites
- Python 3.11+
- Git
- Docker (optional)

Quickstart (local, recommended)
1. Copy environment file:
   cp .env.example .env
   # Edit .env and fill values as needed (no real secrets should be committed)

2. Bootstrap the developer environment (creates a virtualenv and installs dependencies):
   ./scripts/bootstrap.sh

3. Start the local server:
   ./scripts/run-local.sh

4. Verify the health endpoint:
   curl http://localhost:8000/health

Files added in this task
- README.md - this quickstart
- .env.example - example environment variables (no secrets)
- .gitignore, .gitattributes, .editorconfig
- app/main.py - minimal FastAPI app exposing /health and OpenAPI docs
- scripts/bootstrap.sh - sets up virtualenv and installs requirements
- scripts/run-local.sh - runs uvicorn with the app
- requirements.txt - pinned minimal dependencies
- Makefile - convenience commands

Notes
- This is intentionally lightweight and does not implement the full application described in docs/. It provides a reproducible on-ramp for contributors.
- Follow-up tasks will scaffold the full Django/DRF app per the ADR and OpenAPI spec.

