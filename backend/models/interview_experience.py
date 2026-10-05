from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func

from .base import Base


class InterviewExperience(Base):
    __tablename__ = "interview_experiences"

    id = Column(Integer, primary_key=True, index=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id", ondelete="CASCADE"),
        nullable=False
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.id", ondelete="SET NULL"),
        nullable=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="SET NULL"),
        nullable=True
    )

    experience = Column(Text, nullable=False)

    interview_year = Column(Integer, nullable=True)

    result = Column(String(50), nullable=True)

    difficulty = Column(String(50), nullable=True)

    created_at = Column(DateTime, server_default=func.now())