from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InterviewExperienceCreate(BaseModel):
    company_id: int
    role_id: Optional[int] = None
    student_id: Optional[int] = None
    experience: str
    interview_year: Optional[int] = None
    result: Optional[str] = None
    difficulty: Optional[str] = None


class InterviewExperienceUpdate(BaseModel):
    role_id: Optional[int] = None
    student_id: Optional[int] = None
    experience: Optional[str] = None
    interview_year: Optional[int] = None
    result: Optional[str] = None
    difficulty: Optional[str] = None


class InterviewExperienceResponse(BaseModel):
    id: int
    company_id: int
    role_id: Optional[int]
    student_id: Optional[int]
    experience: str
    interview_year: Optional[int]
    result: Optional[str]
    difficulty: Optional[str]
    created_at: Optional[datetime]

    class Config:
        from_attributes = True