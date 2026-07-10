from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Price(BaseModel):
    """A point-in-time quote for a traded instrument."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    symbol: str
    exchange: str
    price: Decimal
    bid: Decimal | None = None
    ask: Decimal | None = None
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: Decimal
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @field_validator("timestamp", mode="before")
    @classmethod
    def ensure_timezone(cls, value: object) -> datetime:
        if isinstance(value, datetime):
            if value.tzinfo is None:
                raise ValueError("timestamp must be timezone-aware")
            return value.astimezone(UTC)
        if isinstance(value, str):
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                raise ValueError("timestamp must be timezone-aware")
            return parsed.astimezone(UTC)
        raise TypeError("timestamp must be a datetime")
