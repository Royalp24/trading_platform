# Backend

FastAPI skeleton with environment-based settings, centralized logging, async
SQLAlchemy session management, Alembic, and a versioned health endpoint.

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
uvicorn app.main:app --reload
```

Run checks with `ruff check .`, `mypy app`, and `pytest`.
