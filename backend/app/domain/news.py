from app.domain.base import DomainModel
from app.domain.types import Symbol, Timestamp


class NewsEvent(DomainModel):
    """Provider-normalized market news or event item."""

    title: str
    description: str | None = None
    impact: str | None = None
    market: str
    symbols: tuple[Symbol, ...]
    source: str
    published_at: Timestamp
