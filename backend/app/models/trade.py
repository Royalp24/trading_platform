from datetime import datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy import DateTime, Enum, ForeignKey, Index, Numeric
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.enums import OrderStatus, OrderType, TradeSide
from app.models.base import BaseModel


class Trade(BaseModel):
    """Recorded paper trade/order event without execution behavior."""

    __tablename__ = "trades"
    __table_args__ = (Index("ix_trades_account_symbol_created", "paper_account_id", "symbol_id"),)

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
    position_id: Mapped[UUID | None] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("positions.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    bot_id: Mapped[UUID | None] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("bots.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    side: Mapped[TradeSide] = mapped_column(Enum(TradeSide, name="trade_side"), nullable=False)
    order_type: Mapped[OrderType] = mapped_column(
        Enum(OrderType, name="order_type"),
        nullable=False,
    )
    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus, name="order_status"),
        nullable=False,
    )
    quantity: Mapped[Decimal] = mapped_column(Numeric(18, 4), nullable=False)
    price: Mapped[Decimal | None] = mapped_column(Numeric(18, 4), nullable=True)
    executed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    paper_account: Mapped["PaperAccount"] = relationship(back_populates="trades")
    symbol: Mapped["Symbol"] = relationship(back_populates="trades")
    position: Mapped["Position | None"] = relationship(back_populates="trades")
    bot: Mapped["Bot | None"] = relationship(back_populates="trades")


from app.models.bot import Bot  # noqa: E402
from app.models.paper_account import PaperAccount  # noqa: E402
from app.models.position import Position  # noqa: E402
from app.models.symbol import Symbol  # noqa: E402
