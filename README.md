# Trading Platform

Docker-first foundation for a provider-independent algorithmic trading platform.
This repository currently contains infrastructure and application skeletons only;
trading logic is intentionally not implemented.

## Prerequisites

- Docker with Docker Compose
- Or, for local development, Python 3.12+ and Node.js 20+

## Quick start

1. Copy `.env.example` to `.env` and replace the placeholder secrets.
2. Run `docker compose up --build`.
3. Open the frontend at <http://localhost:5173>.
4. Check the backend at <http://localhost:8000/api/v1/health>.
5. Open API documentation at <http://localhost:8000/docs>.

The Nginx gateway is available at <http://localhost:8080>.

## Development

Backend commands are documented in `backend/README.md`. Frontend commands are
documented in `frontend/README.md`.

## Scope

See `PROJECT_SPEC.md`. Foundation modules are placeholders that preserve the
specified boundaries. No market-data, strategy, risk, order, or trading behavior
is included.
