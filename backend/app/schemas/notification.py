from datetime import datetime
from uuid import UUID

from app.schemas.base import SchemaModel


class NotificationCreate(SchemaModel):
    user_id: UUID
    channel: str
    title: str
    message: str


class NotificationUpdate(SchemaModel):
    is_read: bool | None = None
    delivered_at: datetime | None = None


class NotificationRead(SchemaModel):
    id: UUID
    user_id: UUID
    channel: str
    title: str
    message: str
    is_read: bool
    delivered_at: datetime | None
    created_at: datetime
    updated_at: datetime


class NotificationResponse(SchemaModel):
    data: NotificationRead
