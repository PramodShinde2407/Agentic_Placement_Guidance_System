from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func

from .base import Base


class OAQuestion(Base):
    __tablename__ = "oa_questions"

    id = Column(Integer, primary_key=True, index=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id", ondelete="CASCADE"),
        nullable=False
    )

    question = Column(Text, nullable=False)

    topic = Column(String(100), nullable=True)

    difficulty = Column(String(50), nullable=True)

    question_type = Column(String(50), nullable=True)

    year = Column(Integer, nullable=True)

    solution = Column(Text, nullable=True)

    created_at = Column(DateTime, server_default=func.now())