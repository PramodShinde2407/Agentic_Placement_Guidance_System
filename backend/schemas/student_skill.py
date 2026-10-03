from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class StudentSkillCreate(BaseModel):
    skill_id: int
    proficiency: str | None = None
    years_experience: Decimal | None = Field(default=None, ge=0)


class StudentSkillUpdate(BaseModel):
    proficiency: str | None = None
    years_experience: Decimal | None = Field(default=None, ge=0)


class StudentSkillResponse(BaseModel):
    student_id: int
    skill_id: int
    proficiency: str | None = None
    years_experience: Decimal | None = None

    model_config = ConfigDict(from_attributes=True)