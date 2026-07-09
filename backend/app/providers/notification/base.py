from abc import ABC, abstractmethod
from typing import Any


class NotificationProvider(ABC):
    """Abstract outbound-notification provider contract."""

    @abstractmethod
    async def send(
        self,
        recipient: str,
        subject: str,
        message: str,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """Send a notification through the configured provider."""
