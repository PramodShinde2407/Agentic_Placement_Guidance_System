from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class PlacementCreate(BaseModel):
    student_id: int
    company_id: int
    role_id: int | None = None
    placement_year: int
    package_lpa: Decimal | None = Field(default=None, ge=0)
    placement_type: str | None = None


class PlacementUpdate(BaseModel):
    student_id: int | None = None
    company_id: int | None = None
    role_id: int | None = None
    placement_year: int | None = None
    package_lpa: Decimal | None = Field(default=None, ge=0)
    placement_type: str | None = None


class PlacementResponse(BaseModel):
    id: int
    student_id: int
    company_id: int
    role_id: int | None = None
    placement_year: int
    package_lpa: Decimal | None = None
    placement_type: str | None = None
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)