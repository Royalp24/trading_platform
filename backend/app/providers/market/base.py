from abc import ABC, abstractmethod
from datetime import datetime
from decimal import Decimal
from typing import Any

from app.core.enums import TimeFrame


class MarketProvider(ABC):
    """Abstract market-data provider contract.

    Implementations must live outside the domain foundation so services can swap
    vendors without changing trading-core or strategy code.
    """

    @abstractmethod
    async def get_live_price(self, symbol: str, exchange: str) -> Decimal:
        """Return the latest available price for a symbol."""

    @abstractmethod
    async def get_historical_data(
        self,
        symbol: str,
        exchange: str,
        timeframe: TimeFrame,
        start_at: datetime,
        end_at: datetime,
    ) -> list[dict[str, Any]]:
        """Return historical candle data for a symbol and timeframe."""

    @abstractmethod
    async def search_symbols(self, query: str) -> list[dict[str, Any]]:
        """Search tradable symbols using provider-specific discovery."""
