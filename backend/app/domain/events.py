from app.core.enums import TradeSide
from app.domain.base import DomainModel
from app.domain.market import Price
from app.domain.signals import Signal
from app.domain.types import Money, PriceValue, Quantity, Symbol, Timestamp, UUIDType


class PriceUpdatedEvent(DomainModel):
    """Event emitted when a normalized price changes."""

    price: Price
    occurred_at: Timestamp


class SignalGeneratedEvent(DomainModel):
    """Event emitted when a strategy produces a signal."""

    signal: Signal
    occurred_at: Timestamp


class TradeOpenedEvent(DomainModel):
    """Event describing a newly opened trade/position."""

    trade_id: UUIDType
    position_id: UUIDType
    symbol: Symbol
    side: TradeSide
    quantity: Quantity
    price: PriceValue
    occurred_at: Timestamp


class TradeClosedEvent(DomainModel):
    """Event describing a closed trade/position."""

    trade_id: UUIDType
    position_id: UUIDType
    symbol: Symbol
    side: TradeSide
    quantity: Quantity
    price: PriceValue
    realized_pnl: Money | None = None
    occurred_at: Timestamp


class PortfolioUpdatedEvent(DomainModel):
    """Event emitted when an account portfolio snapshot changes."""

    account_id: UUIDType
    total_value: Money | None = None
    occurred_at: Timestamp
