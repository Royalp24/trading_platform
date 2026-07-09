from datetime import datetime
from uuid import UUID

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict


class SchemaModel(PydanticBaseModel):
    """Base schema configured for SQLAlchemy model serialization."""

    model_config = ConfigDict(from_attributes=True)


class IdentitySchema(SchemaModel):
    """Public identity fields shared by read schemas."""

    id: UUID


class TimestampSchema(SchemaModel):
    """Public audit timestamps shared by read schemas."""

    created_at: datetime
    updated_at: datetime
