from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import BaseModel


class User(BaseModel):
    """Platform user identity without authentication implementation details."""

    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    display_name: Mapped[str | None] = mapped_column(String(120), nullable=True)

    strategies: Mapped[list["Strategy"]] = relationship(back_populates="user")
    bots: Mapped[list["Bot"]] = relationship(back_populates="user")
    paper_accounts: Mapped[list["PaperAccount"]] = relationship(back_populates="user")
    notifications: Mapped[list["Notification"]] = relationship(back_populates="user")
    system_logs: Mapped[list["SystemLog"]] = relationship(back_populates="user")


from app.models.bot import Bot  # noqa: E402
from app.models.notification import Notification  # noqa: E402
from app.models.paper_account import PaperAccount  # noqa: E402
from app.models.strategy import Strategy  # noqa: E402
from app.models.system_log import SystemLog  # noqa: E402
