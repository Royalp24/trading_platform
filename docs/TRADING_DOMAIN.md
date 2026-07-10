# Trading Domain Objects and Contracts

This document describes the provider-independent trading domain used by the backend.

The purpose of this layer is simple: every internal component communicates through stable,
strongly typed domain objects. External providers such as brokers, market-data vendors, or
fundamental-data vendors are responsible for converting their raw responses into these objects.
No service, strategy, paper-trading module, or analytics module should depend on provider-shaped
dictionaries.

## Architecture Flow

```text
External Provider API
        |
        v
Provider implementation
converts raw response to domain object
        |
        v
Provider interface returns domain object
        |
        v
Service / Strategy / Risk / Analytics layers
consume only domain objects
        |
        v
Repository contracts persist or retrieve domain objects
```

This keeps the platform replaceable. A future Upstox, Zerodha, NSE, news, or notification adapter
can change without forcing the trading core to change.

## Shared Types

`backend/app/domain/types.py` defines reusable aliases such as:

- `PriceValue`
- `Quantity`
- `Percentage`
- `Volume`
- `Money`
- `Symbol`
- `Exchange`
- `TimeFrame`
- `UUIDType`

These aliases make contracts self-documenting and avoid leaking storage/provider concerns into
the trading layer.

## Domain Objects

### Price

Represents a normalized latest market price for a symbol. It includes bid/ask, OHLC values, volume,
and timestamp where providers supply them.

### Candle

Represents a normalized OHLCV candle for a symbol and timeframe.

### FundamentalData

Represents normalized company fundamentals such as market cap, PE, PB, ROE, ROCE, EPS, debt/equity,
growth metrics, and shareholding values.

### NewsEvent

Represents normalized market news or event data. It includes impact, source, related symbols, and
publication time.

### Signal

Represents strategy-generated intent. It is a data contract only and does not execute trades or
perform risk decisions.

### IndicatorValue

Represents a computed indicator value and the parameters used to identify that indicator output.
The current sprint defines the object only; no indicators are implemented here.

## Collection Objects

### PriceSeries

Immutable collection of `Price` objects with a `latest()` helper.

### CandleSeries

Immutable collection of `Candle` objects with a `latest()` helper.

### IndicatorSeries

Immutable collection of `IndicatorValue` objects with a `latest()` helper.

### FundamentalSnapshot

Immutable point-in-time collection of `FundamentalData` with a `for_symbol()` helper.

### PortfolioSnapshot

Immutable account-level portfolio view containing cash balance, positions, and optional total value.
It is a contract for future paper-trading, analytics, and live-trading modules.

## Provider Contracts

Provider interfaces return domain objects, not dictionaries:

- `MarketProvider.get_latest_price()` returns `Price`
- `MarketProvider.get_candles()` returns `CandleSeries`
- `FundamentalProvider.get_fundamentals()` returns `FundamentalData`
- `NewsProvider.get_events()` and `get_news()` return `NewsEvent` collections

Provider implementations are intentionally not included in this sprint.

## Repository Contracts

Repository interfaces define persistence boundaries only:

- `MarketRepository`
- `TradeRepository`
- `StrategyRepository`
- `FundamentalRepository`
- `PortfolioRepository`

No CRUD implementations are included. Future infrastructure code can implement these contracts
against PostgreSQL without changing domain consumers.

## Events

The event models are typed data objects only:

- `PriceUpdatedEvent`
- `SignalGeneratedEvent`
- `TradeOpenedEvent`
- `TradeClosedEvent`
- `PortfolioUpdatedEvent`

No event bus, dispatcher, or side-effecting event logic is implemented in this sprint.
