from datetime import datetime
from uuid import UUID

from app.schemas.base import SchemaModel


class UserCreate(SchemaModel):
    email: str
    display_name: str | None = None


class UserUpdate(SchemaModel):
    email: str | None = None
    display_name: str | None = None


class UserRead(SchemaModel):
    id: UUID
    email: str
    display_name: str | None
    created_at: datetime
    updated_at: datetime


class UserResponse(SchemaModel):
    data: UserRead
