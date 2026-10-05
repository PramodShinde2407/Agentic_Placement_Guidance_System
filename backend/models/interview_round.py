from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, DateTime
from sqlalchemy.sql import func

from .base import Base


class InterviewRound(Base):
    __tablename__ = "interview_rounds"

    id = Column(Integer, primary_key=True, index=True)

    application_id = Column(
        Integer,
        ForeignKey("applications.id", ondelete="CASCADE"),
        nullable=False
    )

    round_name = Column(
        String(100),
        nullable=False
    )

    round_number = Column(
        Integer,
        nullable=False
    )

    round_date = Column(
        Date,
        nullable=True
    )

    status = Column(
        String(50),
        default="pending"
    )

    notes = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )