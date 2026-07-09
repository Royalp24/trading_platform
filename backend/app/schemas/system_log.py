from datetime import datetime
from typing import Any
from uuid import UUID

from app.schemas.base import SchemaModel


class SystemLogCreate(SchemaModel):
    user_id: UUID | None = None
    level: str
    source: str
    message: str
    context: dict[str, Any] | None = None


class SystemLogUpdate(SchemaModel):
    context: dict[str, Any] | None = None


class SystemLogRead(SchemaModel):
    id: UUID
    user_id: UUID | None
    level: str
    source: str
    message: str
    context: dict[str, Any] | None
    created_at: datetime
    updated_at: datetime


class SystemLogResponse(SchemaModel):
    data: SystemLogRead
