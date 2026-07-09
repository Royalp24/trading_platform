from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class FundamentalData(BaseModel):
    """Fundamental metrics for a symbol."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    symbol: str
    market_cap: Decimal | None = None
    pe: Decimal | None = None
    pb: Decimal | None = None
    roe: Decimal | None = None
    roce: Decimal | None = None
    eps: Decimal | None = None
    book_value: Decimal | None = None
    dividend_yield: Decimal | None = None
    debt_to_equity: Decimal | None = None
    current_ratio: Decimal | None = None
    sales_growth: Decimal | None = None
    profit_growth: Decimal | None = None
    promoter_holding: Decimal | None = None
    fii_holding: Decimal | None = None
    dii_holding: Decimal | None = None
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator("updated_at", mode="before")
    @classmethod
    def ensure_timezone(cls, value: object) -> datetime:
        if isinstance(value, datetime):
            if value.tzinfo is None:
                raise ValueError("updated_at must be timezone-aware")
            return value.astimezone(timezone.utc)
        if isinstance(value, str):
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                raise ValueError("updated_at must be timezone-aware")
            return parsed.astimezone(timezone.utc)
        raise TypeError("updated_at must be a datetime")
