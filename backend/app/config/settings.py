from functools import lru_cache
from typing import Literal

from pydantic import AnyHttpUrl, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
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


@lru_cache
def get_settings() -> Settings:
    return Settings()
