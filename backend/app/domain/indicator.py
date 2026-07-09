from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class IndicatorValue(BaseModel):
    """A computed indicator reading for a symbol."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    indicator: str
    parameters: dict[str, object] = Field(default_factory=dict)
    value: Decimal
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
