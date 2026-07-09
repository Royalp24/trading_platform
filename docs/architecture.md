# Foundation architecture

The repository establishes the boundaries from `PROJECT_SPEC.md`:

- API routes validate transport concerns and delegate future behavior.
- Services will orchestrate application use cases.
- Providers will isolate external systems behind replaceable interfaces.
- The trading core modules remain independent from external providers.
- SQLAlchemy and Alembic provide persistence infrastructure.
- Environment variables are the only runtime configuration source.

Only a process-level health endpoint is implemented. Domain behavior is
intentionally absent until each module is requested.
