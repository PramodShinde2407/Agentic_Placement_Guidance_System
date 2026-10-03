from sqlalchemy import Column, Integer, String, Text, DateTime, Numeric, ForeignKey
from .base import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True
    )

    roll_no = Column(
        String(30),
        unique=True
    )

    name = Column(
        String(150),
        nullable=False
    )

    branch = Column(String(100))

    year = Column(Integer)

    cgpa = Column(
        Numeric(4, 2)
    )

    graduation_year = Column(Integer)

    preferred_role_id = Column(
        Integer,
        ForeignKey("roles.id")
    )

    linkedin_url = Column(Text)

    created_at = Column(DateTime)