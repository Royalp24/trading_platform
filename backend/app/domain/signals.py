from app.core.enums import TradeSide
from app.domain.base import DomainModel
from app.domain.types import Percentage, PriceValue, Symbol, Timestamp, UUIDType


class Signal(DomainModel):
    """Strategy-generated intent object consumed by risk and trading layers."""

    strategy_id: UUIDType
    symbol: Symbol
    side: TradeSide
    confidence: Percentage
    entry_price: PriceValue | None = None
    stop_loss: PriceValue | None = None
    target: PriceValue | None = None
    generated_at: Timestamp
