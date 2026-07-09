from uuid import UUID

from sqlalchemy import Enum, ForeignKey, Index, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.enums import BotStatus
from app.models.base import BaseModel


class Bot(BaseModel):
    """Bot configuration linking a user, strategy, and symbol."""

    __tablename__ = "bots"
    __table_args__ = (Index("ix_bots_user_status", "user_id", "status"),)

    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    strategy_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("strategies.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    symbol_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("symbols.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    status: Mapped[BotStatus] = mapped_column(
        Enum(BotStatus, name="bot_status"),
        default=BotStatus.DRAFT,
        nullable=False,
    )

    user: Mapped["User"] = relationship(back_populates="bots")
    strategy: Mapped["Strategy"] = relationship(back_populates="bots")
    symbol: Mapped["Symbol"] = relationship(back_populates="bots")
    positions: Mapped[list["Position"]] = relationship(back_populates="bot")
    trades: Mapped[list["Trade"]] = relationship(back_populates="bot")


from app.models.position import Position  # noqa: E402
from app.models.strategy import Strategy  # noqa: E402
from app.models.symbol import Symbol  # noqa: E402
from app.models.trade import Trade  # noqa: E402
from app.models.user import User  # noqa: E402
