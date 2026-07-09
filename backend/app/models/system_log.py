from typing import Any
from uuid import UUID

from sqlalchemy import JSON, ForeignKey, Index, String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class SystemLog(BaseModel):
    """Persisted operational log entry for diagnostics and audit trails."""

    __tablename__ = "system_logs"
    __table_args__ = (Index("ix_system_logs_level_source", "level", "source"),)

    user_id: Mapped[UUID | None] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    level: Mapped[str] = mapped_column(String(20), nullable=False)
    source: Mapped[str] = mapped_column(String(120), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    context: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)

    user: Mapped["User | None"] = relationship(back_populates="system_logs")


from app.models.user import User  # noqa: E402
