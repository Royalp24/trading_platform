from datetime import datetime
from decimal import Decimal
from uuid import UUID

from app.core.enums import OrderStatus, OrderType, TradeSide
from app.schemas.base import SchemaModel


class TradeCreate(SchemaModel):
    paper_account_id: UUID
    symbol_id: UUID
    position_id: UUID | None = None
    bot_id: UUID | None = None
    side: TradeSide
    order_type: OrderType
    status: OrderStatus
    quantity: Decimal
    price: Decimal | None = None
    executed_at: datetime | None = None


class TradeUpdate(SchemaModel):
    position_id: UUID | None = None
    status: OrderStatus | None = None
    price: Decimal | None = None
    executed_at: datetime | None = None


class TradeRead(SchemaModel):
    id: UUID
    paper_account_id: UUID
    symbol_id: UUID
    position_id: UUID | None
    bot_id: UUID | None
    side: TradeSide
    order_type: OrderType
    status: OrderStatus
    quantity: Decimal
    price: Decimal | None
    executed_at: datetime | None
    created_at: datetime
    updated_at: datetime


class TradeResponse(SchemaModel):
    data: TradeRead
