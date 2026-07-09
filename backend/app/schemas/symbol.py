from datetime import datetime
from uuid import UUID

from app.core.enums import MarketType
from app.schemas.base import SchemaModel


class SymbolCreate(SchemaModel):
    ticker: str
    exchange: str
    name: str
    market_type: MarketType
    is_active: bool = True


class SymbolUpdate(SchemaModel):
    ticker: str | None = None
    exchange: str | None = None
    name: str | None = None
    market_type: MarketType | None = None
    is_active: bool | None = None


class SymbolRead(SchemaModel):
    id: UUID
    ticker: str
    exchange: str
    name: str
    market_type: MarketType
    is_active: bool
    created_at: datetime
    updated_at: datetime


class SymbolResponse(SchemaModel):
    data: SymbolRead
