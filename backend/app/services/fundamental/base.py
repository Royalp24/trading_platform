from abc import ABC, abstractmethod
from typing import Any

from app.providers.fundamental import FundamentalProvider


class FundamentalService(ABC):
    """Service contract for fundamental data caching and retrieval."""

    provider: FundamentalProvider

    @abstractmethod
    async def get_fundamentals(self, symbol: str, exchange: str) -> dict[str, Any]:
        """Return normalized fundamentals for a symbol."""

    @abstractmethod
    async def refresh_symbol(self, symbol: str, exchange: str) -> dict[str, Any]:
        """Refresh fundamentals through the provider boundary."""
