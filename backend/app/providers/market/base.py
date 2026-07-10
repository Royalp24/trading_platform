from abc import ABC, abstractmethod
from datetime import datetime

from app.core.enums import TimeFrame
from app.domain.collections import CandleSeries
from app.domain.market import Price


class MarketProvider(ABC):
    """Abstract market-data provider contract.

    Implementations must live outside the domain foundation so services can swap
    vendors without changing trading-core or strategy code.
    """

    @abstractmethod
    async def get_latest_price(self, symbol: str, exchange: str) -> Price:
        """Return the latest available price as a normalized domain object."""

    @abstractmethod
    async def get_candles(
        self,
        symbol: str,
        exchange: str,
        timeframe: TimeFrame,
        start_at: datetime,
        end_at: datetime,
    ) -> CandleSeries:
        """Return historical candles as a normalized domain collection."""

    @abstractmethod
    async def search_symbols(self, query: str) -> tuple[str, ...]:
        """Search tradable symbol identifiers using provider-specific discovery."""
