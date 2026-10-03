from sqlalchemy import Column, Integer, String, Text, DateTime
from .base import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)

    name = Column(
        String(200),
        nullable=False
    )

    industry = Column(String(100))

    website = Column(Text)

    location = Column(String(150))

    description = Column(Text)

    created_at = Column(DateTime)