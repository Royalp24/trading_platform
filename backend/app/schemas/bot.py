from datetime import datetime
from uuid import UUID

from app.core.enums import BotStatus
from app.schemas.base import SchemaModel


class BotCreate(SchemaModel):
    user_id: UUID
    strategy_id: UUID
    symbol_id: UUID
    name: str
    status: BotStatus = BotStatus.DRAFT


class BotUpdate(SchemaModel):
    strategy_id: UUID | None = None
    symbol_id: UUID | None = None
    name: str | None = None
    status: BotStatus | None = None


class BotRead(SchemaModel):
    id: UUID
    user_id: UUID
    strategy_id: UUID
    symbol_id: UUID
    name: str
    status: BotStatus
    created_at: datetime
    updated_at: datetime


class BotResponse(SchemaModel):
    data: BotRead
