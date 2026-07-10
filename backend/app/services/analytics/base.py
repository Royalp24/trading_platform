from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.collections import PortfolioSnapshot


class AnalyticsService(ABC):
    """Service contract for future portfolio and bot analytics."""

    @abstractmethod
    async def get_account_snapshot(self, paper_account_id: UUID) -> PortfolioSnapshot:
        """Return computed account-level metrics."""

    @abstractmethod
    async def get_bot_snapshot(self, bot_id: UUID) -> PortfolioSnapshot:
        """Return computed bot-level portfolio view."""
