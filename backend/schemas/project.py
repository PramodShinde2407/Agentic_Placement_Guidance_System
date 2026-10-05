from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class ProjectCreate(BaseModel):
    student_id: int
    project_name: str
    description: Optional[str] = None
    technologies: Optional[str] = None
    github_url: Optional[str] = None
    live_url: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class ProjectUpdate(BaseModel):
    project_name: Optional[str] = None
    description: Optional[str] = None
    technologies: Optional[str] = None
    github_url: Optional[str] = None
    live_url: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class ProjectResponse(BaseModel):
    id: int
    student_id: int
    project_name: str
    description: Optional[str]
    technologies: Optional[str]
    github_url: Optional[str]
    live_url: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    created_at: Optional[datetime]

    class Config:
        from_attributes = True