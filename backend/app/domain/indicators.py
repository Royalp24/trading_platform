from typing import Any

from app.domain.base import DomainModel
from app.domain.types import Timestamp


class IndicatorValue(DomainModel):
    """Provider-independent technical indicator value."""

    indicator: str
    parameters: dict[str, Any]
    value: float
    timestamp: Timestamp
