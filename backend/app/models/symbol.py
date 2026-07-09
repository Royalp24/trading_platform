from sqlalchemy import Boolean, Enum, Index, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.enums import MarketType
from app.models.base import BaseModel


class Symbol(BaseModel):
    """Tradable Indian market symbol tracked by the platform."""

    __tablename__ = "symbols"
    __table_args__ = (
        UniqueConstraint("exchange", "ticker", name="uq_symbols_exchange_ticker"),
        Index("ix_symbols_market_type_exchange", "market_type", "exchange"),
    )

    ticker: Mapped[str] = mapped_column(String(32), nullable=False)
    exchange: Mapped[str] = mapped_column(String(32), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    market_type: Mapped[MarketType] = mapped_column(
        Enum(MarketType, name="market_type"),
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    bots: Mapped[list["Bot"]] = relationship(back_populates="symbol")
    positions: Mapped[list["Position"]] = relationship(back_populates="symbol")
    trades: Mapped[list["Trade"]] = relationship(back_populates="symbol")
    technical_snapshots: Mapped[list["TechnicalSnapshot"]] = relationship(back_populates="symbol")
    fundamental_snapshots: Mapped[list["FundamentalSnapshot"]] = relationship(
        back_populates="symbol",
    )


from app.models.bot import Bot  # noqa: E402
from app.models.fundamental_snapshot import FundamentalSnapshot  # noqa: E402
from app.models.position import Position  # noqa: E402
from app.models.technical_snapshot import TechnicalSnapshot  # noqa: E402
from app.models.trade import Trade  # noqa: E402
