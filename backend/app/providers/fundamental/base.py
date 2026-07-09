from abc import ABC, abstractmethod
from typing import Any


class FundamentalProvider(ABC):
    """Abstract fundamental-data provider contract."""

    @abstractmethod
    async def get_fundamentals(self, symbol: str, exchange: str) -> dict[str, Any]:
        """Return provider-normalized fundamentals for a symbol."""

    @abstractmethod
    async def refresh_symbol(self, symbol: str, exchange: str) -> dict[str, Any]:
        """Refresh and return the latest fundamentals for a symbol."""
