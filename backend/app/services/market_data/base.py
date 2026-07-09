from abc import ABC, abstractmethod
from datetime import datetime
from decimal import Decimal
from typing import Any

from app.core.enums import TimeFrame
from app.providers.market import MarketProvider


class MarketDataService(ABC):
    """Service contract for normalized market data access."""

    provider: MarketProvider

    @abstractmethod
    async def get_live_price(self, symbol: str, exchange: str) -> Decimal:
        """Return a normalized live price from the configured market provider."""

    @abstractmethod
    async def get_historical_data(
        self,
        symbol: str,
        exchange: str,
        timeframe: TimeFrame,
        start_at: datetime,
        end_at: datetime,
    ) -> list[dict[str, Any]]:
        """Return normalized historical candles."""

    @abstractmethod
    async def search_symbols(self, query: str) -> list[dict[str, Any]]:
        """Return normalized symbol search results."""
