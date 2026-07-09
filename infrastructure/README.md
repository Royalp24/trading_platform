# Infrastructure

Nginx is the local gateway: `/api/*` is proxied to FastAPI and all other traffic
is proxied to Vite. Docker Compose provisions Nginx, frontend, backend, and
PostgreSQL on an isolated bridge network.
