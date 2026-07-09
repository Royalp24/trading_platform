from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID


class StrategyService(ABC):
    """Service contract for JSON strategy management and validation."""

    @abstractmethod
    async def validate_definition(self, definition: dict[str, Any]) -> None:
        """Validate a strategy definition without evaluating trades."""

    @abstractmethod
    async def get_definition(self, strategy_id: UUID) -> dict[str, Any]:
        """Return a strategy definition by identifier."""
