from datetime import datetime
from typing import Any
from uuid import UUID

from sqlalchemy import JSON, DateTime, Enum, ForeignKey, Index, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.enums import TimeFrame
from app.models.base import BaseModel


class TechnicalSnapshot(BaseModel):
    """Cached technical data payload for a symbol and timeframe."""

    __tablename__ = "technical_snapshots"
    __table_args__ = (
        UniqueConstraint(
            "symbol_id",
            "timeframe",
            "captured_at",
            name="uq_technical_snapshots_symbol_timeframe_captured",
        ),
        Index("ix_technical_snapshots_symbol_timeframe", "symbol_id", "timeframe"),
    )

    symbol_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("symbols.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    timeframe: Mapped[TimeFrame] = mapped_column(Enum(TimeFrame, name="timeframe"), nullable=False)
    captured_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    data: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False)

    symbol: Mapped["Symbol"] = relationship(back_populates="technical_snapshots")


from app.models.symbol import Symbol  # noqa: E402
