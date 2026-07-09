from abc import ABC, abstractmethod
from uuid import UUID


class AnalyticsService(ABC):
    """Service contract for future portfolio and bot analytics."""

    @abstractmethod
    async def get_account_metrics(self, paper_account_id: UUID) -> dict[str, object]:
        """Return computed account-level metrics."""

    @abstractmethod
    async def get_bot_metrics(self, bot_id: UUID) -> dict[str, object]:
        """Return computed bot-level metrics."""
