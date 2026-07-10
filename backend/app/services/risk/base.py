from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.signals import Signal


class RiskService(ABC):
    """Service contract for future risk checks."""

    @abstractmethod
    async def assess_order(
        self,
        paper_account_id: UUID,
        signal: Signal,
    ) -> bool:
        """Assess whether a signal satisfies configured risk constraints."""
