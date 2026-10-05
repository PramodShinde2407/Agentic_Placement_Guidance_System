from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class InterviewRoundCreate(BaseModel):
    application_id: int

    round_name: str

    round_number: int

    round_date: Optional[date] = None

    status: str = "pending"

    notes: Optional[str] = None


class InterviewRoundUpdate(BaseModel):
    round_name: Optional[str] = None

    round_number: Optional[int] = None

    round_date: Optional[date] = None

    status: Optional[str] = None

    notes: Optional[str] = None


class InterviewRoundResponse(BaseModel):
    id: int

    application_id: int

    round_name: str

    round_number: int

    round_date: Optional[date]

    status: str

    notes: Optional[str]

    created_at: Optional[datetime]

    class Config:
        from_attributes = True