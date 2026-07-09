from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID


class RiskService(ABC):
    """Service contract for future risk checks."""

    @abstractmethod
    async def assess_order(
        self,
        paper_account_id: UUID,
        order_payload: dict[str, Any],
    ) -> bool:
        """Assess whether an order payload satisfies configured risk constraints."""
