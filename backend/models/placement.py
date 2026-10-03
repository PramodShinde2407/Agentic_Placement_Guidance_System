from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from .base import Base


class Placement(Base):
    __tablename__ = "placements"

    id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    company_id = Column(
        Integer,
        ForeignKey("companies.id")
    )

    role_id = Column(
        Integer,
        ForeignKey("roles.id")
    )

    placement_year = Column(
        Integer,
        nullable=False
    )

    package_lpa = Column(
        Numeric(8, 2)
    )

    placement_type = Column(
        String(50)
    )

    created_at = Column(DateTime)