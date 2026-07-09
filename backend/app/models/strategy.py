from typing import Any
from uuid import UUID

from sqlalchemy import JSON, Enum, ForeignKey, Index, String, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.enums import StrategyStatus
from app.models.base import BaseModel


class Strategy(BaseModel):
    """Persisted JSON strategy definition without evaluation behavior."""

    __tablename__ = "strategies"
    __table_args__ = (Index("ix_strategies_user_status", "user_id", "status"),)

    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[StrategyStatus] = mapped_column(
        Enum(StrategyStatus, name="strategy_status"),
        default=StrategyStatus.DRAFT,
        nullable=False,
    )
    definition: Mapped[dict[str, Any]] = mapped_column(JSON, nullable=False)

    user: Mapped["User"] = relationship(back_populates="strategies")
    bots: Mapped[list["Bot"]] = relationship(back_populates="strategy")


from app.models.bot import Bot  # noqa: E402
from app.models.user import User  # noqa: E402
