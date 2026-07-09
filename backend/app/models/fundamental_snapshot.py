from datetime import date, datetime
from typing import Any
from uuid import UUID

from sqlalchemy import JSON, Date, DateTime, ForeignKey, Index
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class FundamentalSnapshot(BaseModel):
    """Cached fundamental data payload for a symbol."""

    __tablename__ = "fundamental_snapshots"
    __table_args__ = (
        Index("ix_fundamental_snapshots_symbol_captured", "symbol_id", "captured_at"),
    )

    symbol_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("symbols.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    period_ended_on: Mapped[date | None] = mapped_column(Date, nullable=True)
    captured_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    data: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False)

    symbol: Mapped["Symbol"] = relationship(back_populates="fundamental_snapshots")


from app.models.symbol import Symbol  # noqa: E402
