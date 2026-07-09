from datetime import date, datetime
from typing import Any
from uuid import UUID

from app.schemas.base import SchemaModel


class FundamentalSnapshotCreate(SchemaModel):
    symbol_id: UUID
    period_ended_on: date | None = None
    captured_at: datetime
    data: dict[str, Any]


class FundamentalSnapshotUpdate(SchemaModel):
    period_ended_on: date | None = None
    data: dict[str, Any] | None = None


class FundamentalSnapshotRead(SchemaModel):
    id: UUID
    symbol_id: UUID
    period_ended_on: date | None
    captured_at: datetime
    data: dict[str, Any]
    created_at: datetime
    updated_at: datetime


class FundamentalSnapshotResponse(SchemaModel):
    data: FundamentalSnapshotRead
