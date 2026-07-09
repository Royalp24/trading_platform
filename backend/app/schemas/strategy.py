from datetime import datetime
from typing import Any
from uuid import UUID

from app.core.enums import StrategyStatus
from app.schemas.base import SchemaModel


class StrategyCreate(SchemaModel):
    user_id: UUID
    name: str
    description: str | None = None
    status: StrategyStatus = StrategyStatus.DRAFT
    definition: dict[str, Any]


class StrategyUpdate(SchemaModel):
    name: str | None = None
    description: str | None = None
    status: StrategyStatus | None = None
    definition: dict[str, Any] | None = None


class StrategyRead(SchemaModel):
    id: UUID
    user_id: UUID
    name: str
    description: str | None
    status: StrategyStatus
    definition: dict[str, Any]
    created_at: datetime
    updated_at: datetime


class StrategyResponse(SchemaModel):
    data: StrategyRead
