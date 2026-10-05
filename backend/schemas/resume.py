from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ResumeCreate(BaseModel):
    student_id: int
    file_name: str
    file_path: Optional[str] = None
    extracted_text: Optional[str] = None
    target_role_id: Optional[int] = None
    is_current: bool = False


class ResumeUpdate(BaseModel):
    file_name: Optional[str] = None
    file_path: Optional[str] = None
    extracted_text: Optional[str] = None
    target_role_id: Optional[int] = None
    is_current: Optional[bool] = None


class ResumeResponse(BaseModel):
    id: int
    student_id: int
    file_name: str
    file_path: Optional[str]
    extracted_text: Optional[str]
    target_role_id: Optional[int]
    is_current: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True