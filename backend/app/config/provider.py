from dataclasses import dataclass

from app.config.constants import (
    MARKET_PROVIDER_NSE,
    MARKET_PROVIDER_UPSTOX,
    MARKET_PROVIDER_YAHOO,
    MARKET_PROVIDER_ZERODHA,
)


@dataclass(frozen=True, slots=True)
class ProviderConfig:
    """Provider-related configuration without provider implementation logic."""

    default_market_provider: str
    request_timeout: int
    yahoo_cache_ttl: int
    enable_provider_cache: bool
    log_provider_requests: bool
    default_timezone: str

    def is_yahoo(self) -> bool:
        """Return whether Yahoo Finance is the selected market provider."""

        return self.default_market_provider == MARKET_PROVIDER_YAHOO

    def is_nse(self) -> bool:
        """Return whether NSE is the selected market provider."""

        return self.default_market_provider == MARKET_PROVIDER_NSE

    def is_upstox(self) -> bool:
        """Return whether Upstox is the selected market provider."""

        return self.default_market_provider == MARKET_PROVIDER_UPSTOX

    def is_zerodha(self) -> bool:
        """Return whether Zerodha is the selected market provider."""

        return self.default_market_provider == MARKET_PROVIDER_ZERODHA
