from datetime import UTC, datetime
from typing import Any
from uuid import UUID, uuid4

from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from app.database.base import Base


class UUIDMixin:
    """Adds a UUID primary key to every domain entity."""

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )


class TimestampMixin:
    """Adds creation and update timestamps for auditability."""

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False,
    )


class BaseModel(UUIDMixin, TimestampMixin, Base):
    """Shared base for persisted domain models.

    Table names are derived consistently so future modules can add models without
    repeating infrastructure concerns.
    """

    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:  # noqa: N805
        return cls.__name__.lower()

    def __repr__(self) -> str:
        identity: Any = getattr(self, "id", None)
        return f"{self.__class__.__name__}(id={identity!s})"
