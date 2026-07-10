from abc import ABC, abstractmethod
from datetime import datetime

from app.domain.news import NewsEvent


class NewsProvider(ABC):
    """Abstract news and event provider contract."""

    @abstractmethod
    async def get_events(
        self,
        symbol: str,
        exchange: str,
        start_at: datetime,
        end_at: datetime,
    ) -> tuple[NewsEvent, ...]:
        """Return normalized market events for a symbol."""

    @abstractmethod
    async def get_news(
        self,
        symbol: str,
        exchange: str,
        start_at: datetime,
        end_at: datetime,
    ) -> tuple[NewsEvent, ...]:
        """Return normalized news items for a symbol."""
