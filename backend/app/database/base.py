from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Root SQLAlchemy declarative base.

    Domain models inherit from app.models.base.BaseModel, which adds shared UUID
    and timestamp columns while keeping SQLAlchemy metadata centralized here for
    Alembic and future database tooling.
    """
