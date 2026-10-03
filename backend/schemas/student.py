from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class StudentCreate(BaseModel):
    user_id: int | None = None
    roll_no: str | None = None
    name: str
    branch: str | None = None
    year: int | None = None
    cgpa: Decimal | None = Field(default=None, ge=0, le=10)
    graduation_year: int | None = None
    preferred_role_id: int | None = None
    linkedin_url: str | None = None


class StudentUpdate(BaseModel):
    user_id: int | None = None
    roll_no: str | None = None
    name: str | None = None
    branch: str | None = None
    year: int | None = None
    cgpa: Decimal | None = Field(default=None, ge=0, le=10)
    graduation_year: int | None = None
    preferred_role_id: int | None = None
    linkedin_url: str | None = None


class StudentResponse(BaseModel):
    id: int
    user_id: int | None = None
    roll_no: str | None = None
    name: str
    branch: str | None = None
    year: int | None = None
    cgpa: Decimal | None = None
    graduation_year: int | None = None
    preferred_role_id: int | None = None
    linkedin_url: str | None = None
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)