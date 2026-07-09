from decimal import Decimal
from uuid import UUID

from sqlalchemy import ForeignKey, Index, Numeric, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class PaperAccount(BaseModel):
    """Virtual account boundary for paper positions and trades."""

    __tablename__ = "paper_accounts"
    __table_args__ = (Index("ix_paper_accounts_user", "user_id"),)

    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), default="INR", nullable=False)
    cash_balance: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)

    user: Mapped["User"] = relationship(back_populates="paper_accounts")
    positions: Mapped[list["Position"]] = relationship(back_populates="paper_account")
    trades: Mapped[list["Trade"]] = relationship(back_populates="paper_account")


from app.models.position import Position  # noqa: E402
from app.models.trade import Trade  # noqa: E402
from app.models.user import User  # noqa: E402
