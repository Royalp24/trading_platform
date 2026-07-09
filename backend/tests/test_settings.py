from pytest import MonkeyPatch

from app.config.settings import Settings


def test_settings_can_be_loaded_from_environment(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("APP_NAME", "Test API")

    settings = Settings()

    assert settings.app_name == "Test API"
