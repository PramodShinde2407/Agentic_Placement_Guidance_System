from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class ApplicationCreate(BaseModel):
    student_id: int
    company_id: int
    role_id: int

    application_date: Optional[date] = None

    status: str = "applied"

    current_round: Optional[str] = None

    notes: Optional[str] = None


class ApplicationUpdate(BaseModel):
    status: Optional[str] = None

    current_round: Optional[str] = None

    notes: Optional[str] = None

    application_date: Optional[date] = None


class ApplicationResponse(BaseModel):
    id: int

    student_id: int
    company_id: int
    role_id: int

    application_date: Optional[date]

    status: str

    current_round: Optional[str]

    notes: Optional[str]

    created_at: Optional[datetime]

    class Config:
        from_attributes = True