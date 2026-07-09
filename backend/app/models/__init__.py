"""Persistence models will be added by their requested modules."""

from app.models.base import BaseModel, TimestampMixin, UUIDMixin
from app.models.bot import Bot
from app.models.fundamental_snapshot import FundamentalSnapshot
from app.models.notification import Notification
from app.models.paper_account import PaperAccount
from app.models.position import Position
from app.models.strategy import Strategy
from app.models.symbol import Symbol
from app.models.system_log import SystemLog
from app.models.technical_snapshot import TechnicalSnapshot
from app.models.trade import Trade
from app.models.user import User

__all__ = [
    "BaseModel",
    "Bot",
    "FundamentalSnapshot",
    "Notification",
    "PaperAccount",
    "Position",
    "Strategy",
    "Symbol",
    "SystemLog",
    "TechnicalSnapshot",
    "TimestampMixin",
    "Trade",
    "UUIDMixin",
    "User",
]
