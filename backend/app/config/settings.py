from functools import lru_cache
from typing import Literal

from pydantic import AnyHttpUrl, Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.config.constants import (
    DEFAULT_ENABLE_PROVIDER_CACHE,
    DEFAULT_LOG_PROVIDER_REQUESTS,
    DEFAULT_MARKET_PROVIDER,
    DEFAULT_REQUEST_TIMEOUT,
    DEFAULT_TIMEZONE,
    DEFAULT_YAHOO_CACHE_TTL,
    SUPPORTED_MARKET_PROVIDERS,
)
from app.config.provider import ProviderConfig


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=("../.env", ".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "Trading Platform API"
    app_env: Literal["development", "test", "staging", "production"] = "development"
    app_debug: bool = False
    app_log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    api_v1_prefix: str = "/api/v1"
    backend_cors_origins: list[AnyHttpUrl] = Field(
        default_factory=lambda: [AnyHttpUrl("http://localhost:5173")]
    )

    database_url: str = (
        "postgresql+asyncpg://trading_platform:change-me@localhost:5432/trading_platform"
    )
    jwt_secret: SecretStr
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30

    market_data_provider: str = "unconfigured"
    fundamental_data_provider: str = "unconfigured"
    news_provider: str = "unconfigured"
    notification_provider: str = "unconfigured"

    default_market_provider: str = DEFAULT_MARKET_PROVIDER
    request_timeout: int = Field(default=DEFAULT_REQUEST_TIMEOUT, gt=0)
    yahoo_cache_ttl: int = Field(default=DEFAULT_YAHOO_CACHE_TTL, ge=0)
    enable_provider_cache: bool = DEFAULT_ENABLE_PROVIDER_CACHE
    log_provider_requests: bool = DEFAULT_LOG_PROVIDER_REQUESTS
    default_timezone: str = DEFAULT_TIMEZONE

    @field_validator("default_market_provider")
    @classmethod
    def validate_default_market_provider(cls, value: str) -> str:
        """Ensure provider selection is limited to supported market providers."""

        normalized_provider = value.lower()
        if normalized_provider not in SUPPORTED_MARKET_PROVIDERS:
            supported = ", ".join(SUPPORTED_MARKET_PROVIDERS)
            raise ValueError(f"default_market_provider must be one of: {supported}")
        return normalized_provider

    @property
    def provider_config(self) -> ProviderConfig:
        """Return provider-specific configuration derived from settings."""

        return ProviderConfig(
            default_market_provider=self.default_market_provider,
            request_timeout=self.request_timeout,
            yahoo_cache_ttl=self.yahoo_cache_ttl,
            enable_provider_cache=self.enable_provider_cache,
            log_provider_requests=self.log_provider_requests,
            default_timezone=self.default_timezone,
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
