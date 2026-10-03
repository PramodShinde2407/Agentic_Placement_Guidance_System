from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from .base import Base


class StudentSkill(Base):
    __tablename__ = "student_skills"

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        primary_key=True
    )

    skill_id = Column(
        Integer,
        ForeignKey("skills.id"),
        primary_key=True
    )

    proficiency = Column(String(30))

    years_experience = Column(
        Numeric(4, 2)
    )