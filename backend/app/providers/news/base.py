from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any


class NewsProvider(ABC):
    """Abstract news and event provider contract."""

    @abstractmethod
    async def get_events(
        self,
        symbol: str,
        exchange: str,
        start_at: datetime,
        end_at: datetime,
    ) -> list[dict[str, Any]]:
        """Return market events for a symbol."""

    @abstractmethod
    async def get_news(
        self,
        symbol: str,
        exchange: str,
        start_at: datetime,
        end_at: datetime,
    ) -> list[dict[str, Any]]:
        """Return news items for a symbol."""
