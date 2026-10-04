from pydantic import BaseModel
from typing import Optional


class SkillGapResponse(BaseModel):
    student_id: int
    preferred_role_id: Optional[int]
    required_skill_ids: list[int]
    student_skill_ids: list[int]
    missing_skill_ids: list[int]