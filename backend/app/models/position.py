from datetime import datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy import DateTime, Enum, ForeignKey, Index, Numeric
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.enums import PositionStatus
from app.models.base import BaseModel


class Position(BaseModel):
    """Paper position state; calculations are intentionally outside the model."""

    __tablename__ = "positions"
    __table_args__ = (Index("ix_positions_account_status", "paper_account_id", "status"),)

    paper_account_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("paper_accounts.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    symbol_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("symbols.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    bot_id: Mapped[UUID | None] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("bots.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    status: Mapped[PositionStatus] = mapped_column(
        Enum(PositionStatus, name="position_status"),
        default=PositionStatus.OPEN,
        nullable=False,
    )
    quantity: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    average_price: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    opened_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    closed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    paper_account: Mapped["PaperAccount"] = relationship(back_populates="positions")
    symbol: Mapped["Symbol"] = relationship(back_populates="positions")
    bot: Mapped["Bot | None"] = relationship(back_populates="positions")
    trades: Mapped[list["Trade"]] = relationship(back_populates="position")


from app.models.bot import Bot  # noqa: E402
from app.models.paper_account import PaperAccount  # noqa: E402
from app.models.symbol import Symbol  # noqa: E402
from app.models.trade import Trade  # noqa: E402
