from enum import StrEnum


class MarketType(StrEnum):
    """Supported market segments."""

    EQUITY = "equity"


class OrderType(StrEnum):
    """Order execution styles represented by the domain."""

    MARKET = "market"
    LIMIT = "limit"
    STOP_LOSS = "stop_loss"


class OrderStatus(StrEnum):
    """Lifecycle states for paper orders and recorded trades."""

    PENDING = "pending"
    EXECUTED = "executed"
    CANCELLED = "cancelled"
    REJECTED = "rejected"


class PositionStatus(StrEnum):
    """Lifecycle states for virtual positions."""

    OPEN = "open"
    CLOSED = "closed"


class TradeSide(StrEnum):
    """Trade direction."""

    BUY = "buy"
    SELL = "sell"


class TimeFrame(StrEnum):
    """Canonical market-data candle intervals."""

    ONE_MINUTE = "1m"
    FIVE_MINUTES = "5m"
    FIFTEEN_MINUTES = "15m"
    ONE_HOUR = "1h"
    ONE_DAY = "1d"


class BotStatus(StrEnum):
    """Configured bot states without executing any bot behavior."""

    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    ARCHIVED = "archived"


class StrategyStatus(StrEnum):
    """Configured strategy states."""

    DRAFT = "draft"
    ACTIVE = "active"
    ARCHIVED = "archived"


class SignalType(StrEnum):
    """Signal names future strategy evaluation can emit."""

    BUY = "buy"
    SELL = "sell"
    HOLD = "hold"
