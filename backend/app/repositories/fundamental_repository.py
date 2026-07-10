from abc import ABC, abstractmethod

from app.domain.collections import FundamentalSnapshot
from app.domain.fundamentals import FundamentalData
from app.domain.types import Symbol


class FundamentalRepository(ABC):
    """Persistence contract for normalized fundamental data."""

    @abstractmethod
    async def save(self, fundamentals: FundamentalData) -> None:
        """Persist fundamental data for a symbol."""

    @abstractmethod
    async def get_by_symbol(self, symbol: Symbol) -> FundamentalData | None:
        """Return fundamental data for a symbol when available."""

    @abstractmethod
    async def get_snapshot(self) -> FundamentalSnapshot:
        """Return a point-in-time fundamental snapshot."""
