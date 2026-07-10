from abc import ABC, abstractmethod
from datetime import datetime

from app.core.enums import TimeFrame
from app.domain.collections import CandleSeries
from app.domain.market import Price
from app.providers.market import MarketProvider


class MarketDataService(ABC):
    """Service contract for normalized market data access."""

    provider: MarketProvider

    @abstractmethod
    async def get_latest_price(self, symbol: str, exchange: str) -> Price:
        """Return a normalized live price from the configured market provider."""

    @abstractmethod
    async def get_candles(
        self,
        symbol: str,
        exchange: str,
        timeframe: TimeFrame,
        start_at: datetime,
        end_at: datetime,
    ) -> CandleSeries:
        """Return normalized historical candles."""

    @abstractmethod
    async def search_symbols(self, query: str) -> tuple[str, ...]:
        """Return normalized symbol search results."""
