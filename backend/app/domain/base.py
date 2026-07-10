from pydantic import BaseModel, ConfigDict


class DomainModel(BaseModel):
    """Immutable base class for provider-independent trading domain objects."""

    model_config = ConfigDict(frozen=True)
