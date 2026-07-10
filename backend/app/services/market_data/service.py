from __future__ import annotations

from collections.abc import Awaitable, Callable
from datetime import datetime
from typing import cast

from app.core.enums import TimeFrame
from app.domain.collections import CandleSeries
from app.domain.market import Price
from app.providers.market import MarketProvider
from app.services.market_data.base import MarketDataService


class MarketDataServiceError(RuntimeError):
    """Base exception for market data service failures."""


class MarketDataValidationError(MarketDataServiceError, ValueError):
    """Raised when market data service input validation fails."""


class MarketDataProviderError(MarketDataServiceError):
    """Raised when the configured market provider fails."""


class DefaultMarketDataService(MarketDataService):
    """Default provider-backed market data service implementation."""

    def __init__(self, provider: MarketProvider) -> None:
        self.provider = provider

    async def get_latest_price(self, symbol: str, exchange: str) -> Price:
        """Validate a symbol and return its latest normalized market price."""

        normalized_symbol = self._normalize_symbol(symbol)
        normalized_exchange = self._normalize_exchange(exchange)

        try:
            return await self.provider.get_latest_price(
                symbol=normalized_symbol,
                exchange=normalized_exchange,
            )
        except Exception as exc:
            raise MarketDataProviderError(
                f"Unable to fetch latest price for {normalized_exchange}:{normalized_symbol}"
            ) from exc

    async def get_live_price(self, symbol: str, exchange: str) -> Price:
        """Validate a symbol and return its live normalized market price."""

        return await self.get_latest_price(symbol=symbol, exchange=exchange)

    async def get_candles(
        self,
        symbol: str,
        exchange: str,
        timeframe: TimeFrame,
        start_at: datetime,
        end_at: datetime,
    ) -> CandleSeries:
        """Validate inputs and return normalized historical candles."""

        normalized_symbol = self._normalize_symbol(symbol)
        normalized_exchange = self._normalize_exchange(exchange)
        self._validate_timeframe(timeframe)
        self._validate_date_range(start_at=start_at, end_at=end_at)

        try:
            return await self.provider.get_candles(
                symbol=normalized_symbol,
                exchange=normalized_exchange,
                timeframe=timeframe,
                start_at=start_at,
                end_at=end_at,
            )
        except Exception as exc:
            raise MarketDataProviderError(
                f"Unable to fetch historical data for {normalized_exchange}:{normalized_symbol}"
            ) from exc

    async def get_historical_data(
        self,
        symbol: str,
        exchange: str,
        timeframe: TimeFrame,
        start_at: datetime,
        end_at: datetime,
    ) -> CandleSeries:
        """Validate inputs and return normalized historical candles."""

        return await self.get_candles(
            symbol=symbol,
            exchange=exchange,
            timeframe=timeframe,
            start_at=start_at,
            end_at=end_at,
        )

    async def search_symbols(self, query: str) -> tuple[str, ...]:
        """Validate a search query and return normalized symbol matches."""

        normalized_query = query.strip()
        if not normalized_query:
            raise MarketDataValidationError("Search query cannot be empty")

        try:
            return await self.provider.search_symbols(normalized_query)
        except Exception as exc:
            raise MarketDataProviderError(
                f"Unable to search symbols for query: {normalized_query}"
            ) from exc

    async def get_market_status(self) -> object:
        """Return the configured provider's current market status."""

        provider_method = getattr(self.provider, "get_market_status", None)
        if not callable(provider_method):
            raise MarketDataProviderError(
                "Configured market provider does not expose market status"
            )

        get_market_status = cast(Callable[[], Awaitable[object]], provider_method)
        try:
            return await get_market_status()
        except Exception as exc:
            raise MarketDataProviderError("Unable to fetch market status") from exc

    async def refresh_cache(self) -> None:
        """Refresh provider-backed market data caches when cache support exists."""

        # TODO: Add provider cache refresh orchestration when Phase 1 caching is implemented.
        return None

    @staticmethod
    def _normalize_symbol(symbol: str) -> str:
        normalized_symbol = symbol.strip().upper()
        if not normalized_symbol:
            raise MarketDataValidationError("Symbol cannot be empty")
        return normalized_symbol

    @staticmethod
    def _normalize_exchange(exchange: str) -> str:
        normalized_exchange = exchange.strip().upper()
        if not normalized_exchange:
            raise MarketDataValidationError("Exchange cannot be empty")
        return normalized_exchange

    @staticmethod
    def _validate_timeframe(timeframe: TimeFrame) -> None:
        if not isinstance(timeframe, TimeFrame):
            raise MarketDataValidationError(f"Unsupported timeframe: {timeframe}")

    @staticmethod
    def _validate_date_range(start_at: datetime, end_at: datetime) -> None:
        if start_at >= end_at:
            raise MarketDataValidationError("start_at must be earlier than end_at")
