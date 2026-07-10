from abc import ABC, abstractmethod

from app.domain.fundamentals import FundamentalData


class FundamentalProvider(ABC):
    """Abstract fundamental-data provider contract."""

    @abstractmethod
    async def get_fundamentals(self, symbol: str, exchange: str) -> FundamentalData:
        """Return provider-normalized fundamentals as a domain object."""

    @abstractmethod
    async def refresh_symbol(self, symbol: str, exchange: str) -> FundamentalData:
        """Refresh and return the latest fundamentals for a symbol."""
