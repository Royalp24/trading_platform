#!/usr/bin/env sh
set -eu

cd "$(dirname "$0")/.."

if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env from .env.example; replace placeholder secrets before deployment."
fi

echo "Foundation setup complete. Run: docker compose up --build"
