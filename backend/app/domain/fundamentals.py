from app.domain.base import DomainModel
from app.domain.types import Money, Percentage, PriceValue, Symbol, Timestamp


class FundamentalData(DomainModel):
    """Provider-normalized fundamental metrics for a tradable symbol."""

    symbol: Symbol
    market_cap: Money | None = None
    pe: PriceValue | None = None
    pb: PriceValue | None = None
    roe: Percentage | None = None
    roce: Percentage | None = None
    eps: Money | None = None
    book_value: Money | None = None
    dividend_yield: Percentage | None = None
    debt_to_equity: PriceValue | None = None
    current_ratio: PriceValue | None = None
    sales_growth: Percentage | None = None
    profit_growth: Percentage | None = None
    promoter_holding: Percentage | None = None
    fii_holding: Percentage | None = None
    dii_holding: Percentage | None = None
    updated_at: Timestamp
