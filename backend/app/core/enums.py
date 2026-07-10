from enum import StrEnum


class MarketType(StrEnum):
    """Supported market segments."""

    INDIAN_STOCK = "indian_stock"
    FOREX = "forex"
    CRYPTO = "crypto"
    COMMODITY = "commodity"
    FUTURES = "futures"
    OPTIONS = "options"


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
    THREE_MINUTES = "3m"
    FIVE_MINUTES = "5m"
    TEN_MINUTES = "10m"
    FIFTEEN_MINUTES = "15m"
    THIRTY_MINUTES = "30m"
    FORTY_FIVE_MINUTES = "45m"
    ONE_HOUR = "1h"
    TWO_HOURS = "2h"
    FOUR_HOURS = "4h"
    ONE_DAY = "1d"
    ONE_WEEK = "1w"
    ONE_MONTH = "1M"


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
