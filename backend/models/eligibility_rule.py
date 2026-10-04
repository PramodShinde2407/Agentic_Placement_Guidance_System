from sqlalchemy import Column, Integer, Numeric, Text, Boolean, ForeignKey
from .base import Base


class EligibilityRule(Base):
    __tablename__ = "eligibility_rules"

    id = Column(Integer, primary_key=True, index=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )

    min_10th_marks = Column(Numeric(5, 2), nullable=True)

    min_12th_marks = Column(Numeric(5, 2), nullable=True)

    min_cgpa = Column(Numeric(4, 2), nullable=True)

    allowed_branches = Column(Text, nullable=True)

    max_backlogs = Column(Integer, nullable=True)

    active_backlog = Column(Boolean, default=False)

    passive_backlog = Column(Boolean, default=False)

    graduation_year = Column(Integer, nullable=True)

    amcat_required = Column(Boolean, default=False)

    min_amcat_score = Column(Numeric(6, 2), nullable=True)
    