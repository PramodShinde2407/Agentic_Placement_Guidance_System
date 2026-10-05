from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ChatHistoryCreate(BaseModel):
    student_id: int
    session_id: Optional[str] = None
    user_message: str
    assistant_response: str


class ChatHistoryResponse(BaseModel):
    id: int
    student_id: int
    session_id: Optional[str]
    user_message: str
    assistant_response: str
    created_at: Optional[datetime]

    class Config:
        from_attributes = True