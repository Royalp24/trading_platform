from datetime import datetime
from typing import Any
from uuid import UUID

from app.core.enums import TimeFrame
from app.schemas.base import SchemaModel


class TechnicalSnapshotCreate(SchemaModel):
    symbol_id: UUID
    timeframe: TimeFrame
    captured_at: datetime
    data: dict[str, Any]


class TechnicalSnapshotUpdate(SchemaModel):
    data: dict[str, Any] | None = None


class TechnicalSnapshotRead(SchemaModel):
    id: UUID
    symbol_id: UUID
    timeframe: TimeFrame
    captured_at: datetime
    data: dict[str, Any]
    created_at: datetime
    updated_at: datetime


class TechnicalSnapshotResponse(SchemaModel):
    data: TechnicalSnapshotRead
