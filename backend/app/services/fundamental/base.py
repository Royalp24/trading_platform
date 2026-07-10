from abc import ABC, abstractmethod

from app.domain.fundamentals import FundamentalData
from app.providers.fundamental import FundamentalProvider


class FundamentalService(ABC):
    """Service contract for fundamental data caching and retrieval."""

    provider: FundamentalProvider

    @abstractmethod
    async def get_fundamentals(self, symbol: str, exchange: str) -> FundamentalData:
        """Return normalized fundamentals for a symbol."""

    @abstractmethod
    async def refresh_symbol(self, symbol: str, exchange: str) -> FundamentalData:
        """Refresh fundamentals through the provider boundary."""
