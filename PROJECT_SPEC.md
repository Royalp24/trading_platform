# PROJECT_SPEC.md

# Trading Platform Specification

Version: 1.0

Status: Active

---

# 1. Project Overview

## Objective

Build a professional cloud-based algorithmic trading platform for Indian stocks.

The platform must support:

* Paper Trading
* Live Trading (Future)
* Technical Analysis
* Fundamental Analysis
* Rule-Based Strategy Builder
* Portfolio Analytics
* Multiple Bots
* Multiple Strategies
* Multi-Broker Support
* Dashboard Management

The architecture must be modular, scalable, and provider-independent.

---

# 2. Initial Scope (Phase 1)

Only support:

* Indian Stocks
* Paper Trading
* Live Market Data
* Fundamental Filters
* Technical Indicators
* Dashboard
* Authentication

Do NOT implement live trading in Phase 1.

---

# 3. Core Design Principles

1. Modular Architecture
2. Provider-Based Design
3. No Vendor Lock-in
4. Rule-Based Strategies
5. Docker First
6. API First
7. Production Ready
8. Strong Typing
9. Clean Code
10. Testable Components

---

# 4. High-Level Architecture

Frontend

↓

FastAPI REST API

↓

Trading Core

↓

Service Layer

↓

Provider Layer

↓

Database

The Trading Core must never communicate directly with external APIs.

---

# 5. Technology Stack

Backend

* Python 3.12+
* FastAPI
* SQLAlchemy
* Alembic
* PostgreSQL
* APScheduler
* Pydantic
* JWT Authentication

Frontend

* React
* Vite
* TypeScript
* TailwindCSS
* shadcn/ui
* Recharts

Infrastructure

* Docker
* Docker Compose
* Nginx

Deployment

* Oracle Cloud Free

Version Control

* Git
* GitHub

---

# 6. Folder Structure

```
trading-platform/

backend/
frontend/
docs/
scripts/
infrastructure/

docker-compose.yml
README.md
PROJECT_SPEC.md
.env.example
.gitignore
```

Backend structure

```
backend/app/

api/
core/
config/
database/
models/
schemas/
services/
providers/
strategies/
indicators/
paper_trading/
analytics/
notifications/
scheduler/
utils/
```

---

# 7. Architecture Layers

## API Layer

Responsibilities

* Receive requests
* Validate requests
* Return responses

No business logic.

---

## Service Layer

Responsible for:

* Market Data
* Fundamentals
* Indicators
* Strategy Evaluation
* Paper Trading
* Analytics

---

## Provider Layer

Responsible for external integrations.

Examples

Market Provider

Fundamental Provider

News Provider

Notification Provider

Services communicate with providers.

Strategies never communicate with providers.

---

## Trading Core

Responsible for:

Strategy Evaluation

Risk Management

Position Management

Signal Generation

Paper Trading

---

# 8. Strategy System

Strategies are stored as JSON.

No strategy should require editing Python code.

Example

```
{
  "technical": [],
  "fundamental": [],
  "risk": {}
}
```

The Strategy Engine must evaluate JSON rules.

Support:

* AND
* OR
* NOT

Future support:

Nested groups

Custom expressions

---

# 9. Data Flow

Market Provider

↓

MarketDataService

↓

Indicator Engine

↓

Strategy Engine

↓

Risk Manager

↓

Paper Trading Engine

↓

Database

↓

Dashboard

---

# 10. Market Data Service

Responsibilities

* Live Price
* Historical Candles
* Symbol Search
* Timeframes

The implementation must be provider-independent.

---

# 11. Fundamental Service

Responsibilities

* Market Cap
* PE
* PB
* ROE
* ROCE
* Book Value
* EPS
* Debt/Equity
* Dividend Yield
* Sales Growth
* Profit Growth
* Shareholding

Fundamental data should be cached in PostgreSQL.

Strategies read only from the database.

---

# 12. Indicator Engine

Supported Indicators

EMA

SMA

RSI

MACD

ATR

VWAP

Bollinger Bands

Supertrend

ADX

More indicators can be added later.

---

# 13. Paper Trading Engine

Responsibilities

* Buy
* Sell
* Stop Loss
* Take Profit
* Position Sizing
* Trailing Stop
* Virtual Portfolio
* Profit & Loss

No real broker orders.

---

# 14. Risk Manager

Support

* Max Risk %
* Max Daily Loss
* Max Open Positions
* Position Size
* Drawdown Limit
* Cooldown Rules

---

# 15. Analytics Engine

Metrics

* Win Rate
* Profit Factor
* Sharpe Ratio
* Max Drawdown
* Equity Curve
* Monthly Returns
* Daily Returns
* Trade Distribution

---

# 16. Dashboard

Pages

* Login
* Dashboard
* Bots
* Strategies
* Markets
* Trades
* Analytics
* Settings

---

# 17. Database

Main tables

Users

Bots

Strategies

Symbols

Technical Data

Fundamental Data

Paper Orders

Trades

Positions

Logs

Performance

Notifications

---

# 18. Coding Standards

Use:

* Python type hints
* SOLID principles
* Dependency Injection
* Repository Pattern where appropriate
* Async APIs where beneficial

Avoid:

* Global variables
* Business logic inside API routes
* Hardcoded configuration
* Duplicate code

---

# 19. Configuration

All configuration must come from environment variables.

Examples

Database URL

JWT Secret

API Keys

Provider Selection

Debug Mode

Never hardcode secrets.

---

# 20. Logging

Implement centralized logging.

Levels

INFO

WARNING

ERROR

CRITICAL

Store logs for debugging.

---

# 21. Testing

Every module should be testable independently.

Include

* Unit Tests
* Integration Tests

---

# 22. Development Rules

Never generate code outside the requested module.

Never modify unrelated modules.

Keep changes isolated.

Always preserve architecture.

Always follow PROJECT_SPEC.md.

---

# 23. Development Workflow

For every implementation:

1. Read PROJECT_SPEC.md
2. Implement only the requested module
3. Do not implement future modules
4. Keep code modular
5. Add documentation where necessary
6. Ensure compatibility with the overall architecture

---

# 24. Future Phases

Phase 2

* Multi-broker support
* News engine
* Fundamental scanner
* Notifications

Phase 3

* Backtesting
* Strategy optimization
* Portfolio analysis

Phase 4

* Live trading
* Broker integrations
* Portfolio management

Phase 5

* AI strategy assistant
* AI trade journal
* AI optimization
* AI market insights

---

# 25. Guiding Principle

Every component must be replaceable without affecting the rest of the system.

The platform should never depend on a specific broker, API, or data provider.

Services communicate through interfaces.

The architecture should remain stable even as providers, brokers, or markets change.
