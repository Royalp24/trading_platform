from abc import ABC, abstractmethod

from app.domain.collections import PortfolioSnapshot
from app.domain.types import UUIDType


class PortfolioRepository(ABC):
    """Persistence contract for account portfolio snapshots."""

    @abstractmethod
    async def save_snapshot(self, snapshot: PortfolioSnapshot) -> None:
        """Persist a portfolio snapshot."""

    @abstractmethod
    async def get_latest_snapshot(self, account_id: UUIDType) -> PortfolioSnapshot | None:
        """Return the latest portfolio snapshot for an account."""
