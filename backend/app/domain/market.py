from app.domain.base import DomainModel
from app.domain.types import Exchange, PriceValue, Symbol, TimeFrame, Timestamp, Volume


class Price(DomainModel):
    """Provider-normalized latest market price for a symbol."""

    symbol: Symbol
    exchange: Exchange
    price: PriceValue
    bid: PriceValue | None = None
    ask: PriceValue | None = None
    open: PriceValue | None = None
    high: PriceValue | None = None
    low: PriceValue | None = None
    close: PriceValue | None = None
    volume: Volume | None = None
    timestamp: Timestamp


class Candle(DomainModel):
    """Provider-normalized OHLCV candle."""

    symbol: Symbol
    timeframe: TimeFrame
    open: PriceValue
    high: PriceValue
    low: PriceValue
    close: PriceValue
    volume: Volume
    timestamp: Timestamp
