from sqlalchemy import Column, Integer, String, Date, ForeignKey
from backend.models.base import Base


class CompanyVisit(Base):
    __tablename__ = "company_visits"

    id = Column(Integer, primary_key=True, index=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False
    )

    visit_year = Column(
        Integer,
        nullable=False
    )

    visit_date = Column(
        Date,
        nullable=True
    )

    drive_type = Column(
        String(50),
        nullable=True
    )