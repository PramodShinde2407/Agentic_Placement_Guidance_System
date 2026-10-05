from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from .base import Base


class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False
    )

    session_id = Column(String(100), nullable=True)

    user_message = Column(Text, nullable=False)

    assistant_response = Column(Text, nullable=False)

    created_at = Column(DateTime, server_default=func.now())