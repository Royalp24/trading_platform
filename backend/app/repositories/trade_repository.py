from abc import ABC, abstractmethod

from app.domain.events import TradeClosedEvent, TradeOpenedEvent
from app.domain.types import UUIDType


class TradeRepository(ABC):
    """Persistence contract for trade-domain event records."""

    @abstractmethod
    async def record_opened(self, event: TradeOpenedEvent) -> None:
        """Persist a trade-opened event."""

    @abstractmethod
    async def record_closed(self, event: TradeClosedEvent) -> None:
        """Persist a trade-closed event."""

    @abstractmethod
    async def exists(self, trade_id: UUIDType) -> bool:
        """Return whether a trade record exists."""
