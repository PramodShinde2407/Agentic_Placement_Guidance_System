from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    role = Column(String(30), nullable=False, default="student")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)