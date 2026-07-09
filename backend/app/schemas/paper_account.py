from datetime import datetime
from decimal import Decimal
from uuid import UUID

from app.schemas.base import SchemaModel


class PaperAccountCreate(SchemaModel):
    user_id: UUID
    name: str
    currency: str = "INR"
    cash_balance: Decimal


class PaperAccountUpdate(SchemaModel):
    name: str | None = None
    currency: str | None = None
    cash_balance: Decimal | None = None


class PaperAccountRead(SchemaModel):
    id: UUID
    user_id: UUID
    name: str
    currency: str
    cash_balance: Decimal
    created_at: datetime
    updated_at: datetime


class PaperAccountResponse(SchemaModel):
    data: PaperAccountRead
