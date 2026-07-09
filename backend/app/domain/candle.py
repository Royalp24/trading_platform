from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Candle(BaseModel):
    """A market candle for a symbol and timeframe."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    symbol: str
    exchange: str
    timeframe: str
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: Decimal
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator("timestamp", mode="before")
    @classmethod
    def ensure_timezone(cls, value: object) -> datetime:
        if isinstance(value, datetime):
            if value.tzinfo is None:
                raise ValueError("timestamp must be timezone-aware")
            return value.astimezone(timezone.utc)
        if isinstance(value, str):
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                raise ValueError("timestamp must be timezone-aware")
            return parsed.astimezone(timezone.utc)
        raise TypeError("timestamp must be a datetime")

    @property
    def is_bullish(self) -> bool:
        """True when the candle closes above its open."""
        return self.close > self.open

    @property
    def is_bearish(self) -> bool:
        """True when the candle closes below its open."""
        return self.close < self.open

    @property
    def body_size(self) -> Decimal:
        """Absolute size of the candle body."""
        return abs(self.close - self.open)

    @property
    def range_size(self) -> Decimal:
        """Total high-to-low range of the candle."""
        return self.high - self.low
