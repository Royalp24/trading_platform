from app.core.enums import PositionStatus, TradeSide
from app.domain.base import DomainModel
from app.domain.fundamentals import FundamentalData
from app.domain.indicators import IndicatorValue
from app.domain.market import Candle, Price
from app.domain.types import Money, PriceValue, Quantity, Symbol, UUIDType


class PriceSeries(DomainModel):
    """Immutable collection of price observations."""

    symbol: Symbol
    prices: tuple[Price, ...]

    def latest(self) -> Price | None:
        """Return the newest price by timestamp when available."""

        return max(self.prices, key=lambda price: price.timestamp, default=None)


class CandleSeries(DomainModel):
    """Immutable collection of OHLCV candles for a symbol/timeframe."""

    symbol: Symbol
    candles: tuple[Candle, ...]

    def latest(self) -> Candle | None:
        """Return the newest candle by timestamp when available."""

        return max(self.candles, key=lambda candle: candle.timestamp, default=None)


class IndicatorSeries(DomainModel):
    """Immutable collection of indicator values."""

    indicator: str
    values: tuple[IndicatorValue, ...]

    def latest(self) -> IndicatorValue | None:
        """Return the newest indicator value by timestamp when available."""

        return max(self.values, key=lambda value: value.timestamp, default=None)


class FundamentalSnapshot(DomainModel):
    """Point-in-time collection of fundamental data objects."""

    fundamentals: tuple[FundamentalData, ...]

    def for_symbol(self, symbol: Symbol) -> FundamentalData | None:
        """Return fundamentals for a symbol when present."""

        return next((item for item in self.fundamentals if item.symbol == symbol), None)


class PortfolioPosition(DomainModel):
    """Provider-independent position view used inside portfolio snapshots."""

    position_id: UUIDType
    symbol: Symbol
    side: TradeSide
    status: PositionStatus
    quantity: Quantity
    average_price: PriceValue
    market_price: PriceValue | None = None


class PortfolioSnapshot(DomainModel):
    """Immutable account portfolio view for paper/live trading layers."""

    account_id: UUIDType
    cash_balance: Money
    positions: tuple[PortfolioPosition, ...]
    total_value: Money | None = None

    def open_positions(self) -> tuple[PortfolioPosition, ...]:
        """Return positions currently marked open."""

        return tuple(
            position for position in self.positions if position.status == PositionStatus.OPEN
        )
