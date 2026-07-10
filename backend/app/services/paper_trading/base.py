from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.collections import PortfolioSnapshot


class PaperTradingService(ABC):
    """Service contract for future virtual portfolio operations."""

    @abstractmethod
    async def get_account_state(self, paper_account_id: UUID) -> PortfolioSnapshot:
        """Return account state for downstream dashboard and analytics modules."""

    @abstractmethod
    async def record_trade(self, trade_id: UUID) -> None:
        """Record a paper trade event without broker integration."""
