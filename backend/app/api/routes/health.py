from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Report API process readiness without invoking external dependencies."""
    return HealthResponse(status="ok", service="backend")
