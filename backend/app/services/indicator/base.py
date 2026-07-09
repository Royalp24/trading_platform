from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID

from app.core.enums import TimeFrame


class IndicatorService(ABC):
    """Service contract for future technical snapshot generation."""

    @abstractmethod
    async def create_snapshot(
        self,
        symbol_id: UUID,
        timeframe: TimeFrame,
        candles: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Create a technical snapshot payload from market data."""
