from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base


class RoleSkill(Base):
    __tablename__ = "role_skills"

    role_id = Column(
        Integer,
        ForeignKey("roles.id"),
        primary_key=True
    )

    skill_id = Column(
        Integer,
        ForeignKey("skills.id"),
        primary_key=True
    )

    importance = Column(
        String(30),
        default="required"
    )