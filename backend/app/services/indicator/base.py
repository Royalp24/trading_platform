from abc import ABC, abstractmethod
from uuid import UUID

from app.core.enums import TimeFrame
from app.domain.collections import CandleSeries, IndicatorSeries


class IndicatorService(ABC):
    """Service contract for future technical snapshot generation."""

    @abstractmethod
    async def create_snapshot(
        self,
        symbol_id: UUID,
        timeframe: TimeFrame,
        candles: CandleSeries,
    ) -> IndicatorSeries:
        """Create a technical snapshot payload from market data."""
