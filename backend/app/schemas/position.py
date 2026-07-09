from datetime import datetime
from decimal import Decimal
from uuid import UUID

from app.core.enums import PositionStatus
from app.schemas.base import SchemaModel


class PositionCreate(SchemaModel):
    paper_account_id: UUID
    symbol_id: UUID
    bot_id: UUID | None = None
    status: PositionStatus = PositionStatus.OPEN
    quantity: Decimal
    average_price: Decimal
    opened_at: datetime
    closed_at: datetime | None = None


class PositionUpdate(SchemaModel):
    status: PositionStatus | None = None
    quantity: Decimal | None = None
    average_price: Decimal | None = None
    closed_at: datetime | None = None


class PositionRead(SchemaModel):
    id: UUID
    paper_account_id: UUID
    symbol_id: UUID
    bot_id: UUID | None
    status: PositionStatus
    quantity: Decimal
    average_price: Decimal
    opened_at: datetime
    closed_at: datetime | None
    created_at: datetime
    updated_at: datetime


class PositionResponse(SchemaModel):
    data: PositionRead
