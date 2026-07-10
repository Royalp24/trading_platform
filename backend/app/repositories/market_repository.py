from abc import ABC, abstractmethod

from app.domain.collections import CandleSeries, PriceSeries
from app.domain.market import Price
from app.domain.types import Symbol


class MarketRepository(ABC):
    """Persistence contract for normalized market-domain data."""

    @abstractmethod
    async def save_price(self, price: Price) -> None:
        """Persist a normalized price observation."""

    @abstractmethod
    async def get_prices(self, symbol: Symbol) -> PriceSeries:
        """Return persisted prices for a symbol."""

    @abstractmethod
    async def save_candles(self, candles: CandleSeries) -> None:
        """Persist normalized candle observations."""

    @abstractmethod
    async def get_candles(self, symbol: Symbol) -> CandleSeries:
        """Return persisted candles for a symbol."""
