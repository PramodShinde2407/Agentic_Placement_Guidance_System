from pydantic import BaseModel
from datetime import date
from typing import Optional


class CompanyVisitCreate(BaseModel):
    company_id: int
    visit_year: int
    visit_date: Optional[date] = None
    drive_type: Optional[str] = None


class CompanyVisitUpdate(BaseModel):
    visit_year: Optional[int] = None
    visit_date: Optional[date] = None
    drive_type: Optional[str] = None


class CompanyVisitResponse(BaseModel):
    id: int
    company_id: int
    visit_year: int
    visit_date: Optional[date]
    drive_type: Optional[str]

    class Config:
        from_attributes = True