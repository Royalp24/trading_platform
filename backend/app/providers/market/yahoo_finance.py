from __future__ import annotations

import asyncio
from datetime import UTC, datetime, time
from decimal import Decimal, InvalidOperation
from enum import StrEnum
from importlib import import_module
from types import ModuleType
from typing import Any
from zoneinfo import ZoneInfo

from app.core.enums import TimeFrame
from app.domain.collections import CandleSeries
from app.domain.market import Candle, Price
from app.providers.market.base import MarketProvider


class MarketStatus(StrEnum):
    """Simple market status values for provider-level status checks."""

    OPEN = "open"
    CLOSED = "closed"


class YahooFinanceProviderError(RuntimeError):
    """Raised when Yahoo Finance data cannot be converted into domain objects."""


class YahooFinanceProvider(MarketProvider):
    """Market data provider backed by yfinance.

    The provider is the only module allowed to understand Yahoo Finance response
    shapes. All public methods return domain models or typed primitives.
    """

    _TIMEFRAME_TO_YAHOO_INTERVAL: dict[TimeFrame, str] = {
        TimeFrame.ONE_MINUTE: "1m",
        TimeFrame.THREE_MINUTES: "2m",
        TimeFrame.FIVE_MINUTES: "5m",
        TimeFrame.TEN_MINUTES: "15m",
        TimeFrame.FIFTEEN_MINUTES: "15m",
        TimeFrame.THIRTY_MINUTES: "30m",
        TimeFrame.FORTY_FIVE_MINUTES: "60m",
        TimeFrame.ONE_HOUR: "60m",
        TimeFrame.TWO_HOURS: "90m",
        TimeFrame.FOUR_HOURS: "1h",
        TimeFrame.ONE_DAY: "1d",
        TimeFrame.ONE_WEEK: "1wk",
        TimeFrame.ONE_MONTH: "1mo",
    }

    def __init__(self, *, default_exchange: str = "NSE", timezone: str = "Asia/Kolkata") -> None:
        self.default_exchange = default_exchange
        self.timezone = ZoneInfo(timezone)

    async def get_latest_price(self, symbol: str, exchange: str) -> Price:
        """Return the latest Yahoo Finance quote as a normalized Price object."""

        ticker_symbol = self._to_yahoo_symbol(symbol, exchange)
        ticker = self._ticker(ticker_symbol)
        history = await asyncio.to_thread(ticker.history, period="1d", interval="1m")

        if self._is_empty_frame(history):
            raise YahooFinanceProviderError(f"No live price data returned for {ticker_symbol}")

        row = history.iloc[-1]
        timestamp = self._timestamp_from_index(history.index[-1])
        close_price = self._decimal_from_row(row, "Close")
        fast_info = self._safe_fast_info(ticker)

        return Price(
            symbol=symbol,
            exchange=exchange,
            price=self._decimal_from_mapping(fast_info, "last_price") or close_price,
            bid=self._decimal_from_mapping(fast_info, "bid"),
            ask=self._decimal_from_mapping(fast_info, "ask"),
            open=self._decimal_from_row(row, "Open"),
            high=self._decimal_from_row(row, "High"),
            low=self._decimal_from_row(row, "Low"),
            close=close_price,
            volume=self._decimal_from_row(row, "Volume"),
            timestamp=timestamp,
        )

    async def get_live_price(self, symbol: str, exchange: str) -> Price:
        """Return the latest Yahoo Finance quote as a normalized Price object."""

        return await self.get_latest_price(symbol=symbol, exchange=exchange)

    async def get_candles(
        self,
        symbol: str,
        exchange: str,
        timeframe: TimeFrame,
        start_at: datetime,
        end_at: datetime,
    ) -> CandleSeries:
        """Return Yahoo Finance OHLCV data as a normalized CandleSeries."""

        ticker_symbol = self._to_yahoo_symbol(symbol, exchange)
        interval = self._to_yahoo_interval(timeframe)
        ticker = self._ticker(ticker_symbol)

        history = await asyncio.to_thread(
            ticker.history,
            start=start_at,
            end=end_at,
            interval=interval,
        )

        if self._is_empty_frame(history):
            raise YahooFinanceProviderError(f"No historical data returned for {ticker_symbol}")

        candles = tuple(
            Candle(
                symbol=symbol,
                timeframe=timeframe,
                open=self._decimal_from_row(row, "Open"),
                high=self._decimal_from_row(row, "High"),
                low=self._decimal_from_row(row, "Low"),
                close=self._decimal_from_row(row, "Close"),
                volume=self._decimal_from_row(row, "Volume"),
                timestamp=self._timestamp_from_index(index),
            )
            for index, row in history.iterrows()
        )

        return CandleSeries(symbol=symbol, candles=candles)

    async def get_historical_data(
        self,
        symbol: str,
        exchange: str,
        timeframe: TimeFrame,
        start_at: datetime,
        end_at: datetime,
    ) -> CandleSeries:
        """Return Yahoo Finance OHLCV data as a normalized CandleSeries."""

        return await self.get_candles(
            symbol=symbol,
            exchange=exchange,
            timeframe=timeframe,
            start_at=start_at,
            end_at=end_at,
        )

    async def search_symbols(self, query: str) -> tuple[str, ...]:
        """Search symbols through yfinance when available.

        yfinance search support varies by version. When the helper is unavailable,
        this method returns a documented Phase 1 placeholder: the normalized query
        as a single ticker symbol. No website scraping is performed.
        """

        normalized_query = query.strip().upper()
        if not normalized_query:
            return ()

        yfinance = self._yfinance()
        search = getattr(yfinance, "Search", None)
        if search is None:
            return (normalized_query,)

        try:
            result = await asyncio.to_thread(search, normalized_query)
            quotes = getattr(result, "quotes", None) or ()
        except Exception as exc:  # pragma: no cover - network/provider failure path
            raise YahooFinanceProviderError("Yahoo Finance symbol search failed") from exc

        symbols = tuple(
            quote_symbol
            for quote in quotes
            if isinstance((quote_symbol := quote.get("symbol")), str)
        )
        return symbols or (normalized_query,)

    async def get_market_status(self) -> MarketStatus:
        """Return a simple weekday/session market status.

        Holiday and special-session calculations are intentionally out of scope
        for this first provider implementation.
        """

        now = datetime.now(self.timezone)
        if now.weekday() >= 5:
            return MarketStatus.CLOSED

        market_open = time(hour=9, minute=15, tzinfo=self.timezone)
        market_close = time(hour=15, minute=30, tzinfo=self.timezone)
        if market_open <= now.timetz() <= market_close:
            return MarketStatus.OPEN
        return MarketStatus.CLOSED

    def _ticker(self, ticker_symbol: str) -> Any:
        try:
            return self._yfinance().Ticker(ticker_symbol)
        except Exception as exc:  # pragma: no cover - defensive provider boundary
            raise YahooFinanceProviderError(f"Unable to initialize ticker {ticker_symbol}") from exc

    @staticmethod
    def _yfinance() -> ModuleType:
        try:
            return import_module("yfinance")
        except ModuleNotFoundError as exc:  # pragma: no cover - dependency installation guard
            raise YahooFinanceProviderError(
                "yfinance is required for YahooFinanceProvider. Install backend dependencies."
            ) from exc

    @staticmethod
    def _to_yahoo_symbol(symbol: str, exchange: str) -> str:
        normalized_symbol = symbol.strip().upper()
        normalized_exchange = exchange.strip().upper()

        if "." in normalized_symbol:
            return normalized_symbol
        if normalized_exchange == "NSE":
            return f"{normalized_symbol}.NS"
        if normalized_exchange == "BSE":
            return f"{normalized_symbol}.BO"
        return normalized_symbol

    def _to_yahoo_interval(self, timeframe: TimeFrame) -> str:
        try:
            return self._TIMEFRAME_TO_YAHOO_INTERVAL[timeframe]
        except KeyError as exc:
            raise YahooFinanceProviderError(
                f"Unsupported Yahoo Finance timeframe: {timeframe}"
            ) from exc

    @staticmethod
    def _is_empty_frame(frame: Any) -> bool:
        return bool(getattr(frame, "empty", True))

    @staticmethod
    def _timestamp_from_index(value: Any) -> datetime:
        if hasattr(value, "to_pydatetime"):
            value = value.to_pydatetime()
        if not isinstance(value, datetime):
            raise YahooFinanceProviderError("Yahoo Finance returned an invalid timestamp")
        if value.tzinfo is None:
            return value.replace(tzinfo=UTC)
        return value.astimezone(UTC)

    @staticmethod
    def _safe_fast_info(ticker: Any) -> Any:
        try:
            return ticker.fast_info
        except Exception:
            return {}

    @staticmethod
    def _decimal_from_mapping(mapping: Any, key: str) -> Decimal | None:
        if not hasattr(mapping, "get"):
            return None
        value = mapping.get(key)
        if value is None:
            return None
        return YahooFinanceProvider._to_decimal(value, field_name=key)

    @staticmethod
    def _decimal_from_row(row: Any, field_name: str) -> Decimal:
        try:
            value = row[field_name]
        except Exception as exc:
            raise YahooFinanceProviderError(
                f"Yahoo Finance response missing required field: {field_name}"
            ) from exc
        return YahooFinanceProvider._to_decimal(value, field_name=field_name)

    @staticmethod
    def _to_decimal(value: Any, *, field_name: str) -> Decimal:
        try:
            decimal_value = Decimal(str(value))
        except (InvalidOperation, ValueError) as exc:
            raise YahooFinanceProviderError(
                f"Yahoo Finance returned invalid numeric value for {field_name}"
            ) from exc
        if not decimal_value.is_finite():
            raise YahooFinanceProviderError(
                f"Yahoo Finance returned non-finite numeric value for {field_name}"
            )
        return decimal_value
