from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OAQuestionCreate(BaseModel):
    company_id: int
    question: str
    topic: Optional[str] = None
    difficulty: Optional[str] = None
    question_type: Optional[str] = None
    year: Optional[int] = None
    solution: Optional[str] = None


class OAQuestionUpdate(BaseModel):
    question: Optional[str] = None
    topic: Optional[str] = None
    difficulty: Optional[str] = None
    question_type: Optional[str] = None
    year: Optional[int] = None
    solution: Optional[str] = None


class OAQuestionResponse(BaseModel):
    id: int
    company_id: int
    question: str
    topic: Optional[str]
    difficulty: Optional[str]
    question_type: Optional[str]
    year: Optional[int]
    solution: Optional[str]
    created_at: Optional[datetime]

    class Config:
        from_attributes = True