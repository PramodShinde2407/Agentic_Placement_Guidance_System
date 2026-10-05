from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date, DateTime
from sqlalchemy.sql import func

from .base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False
    )

    project_name = Column(String(200), nullable=False)

    description = Column(Text, nullable=True)

    technologies = Column(Text, nullable=True)

    github_url = Column(Text, nullable=True)

    live_url = Column(Text, nullable=True)

    start_date = Column(Date, nullable=True)

    end_date = Column(Date, nullable=True)

    created_at = Column(DateTime, server_default=func.now())