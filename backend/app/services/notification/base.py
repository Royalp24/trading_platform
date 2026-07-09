from abc import ABC, abstractmethod
from uuid import UUID

from app.providers.notification import NotificationProvider


class NotificationService(ABC):
    """Service contract for notification orchestration."""

    provider: NotificationProvider

    @abstractmethod
    async def send(self, notification_id: UUID) -> None:
        """Dispatch a notification through the configured provider boundary."""
