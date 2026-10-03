from pydantic import BaseModel, ConfigDict


class RoleSkillCreate(BaseModel):
    skill_id: int
    importance: str = "required"


class RoleSkillUpdate(BaseModel):
    importance: str | None = None


class RoleSkillResponse(BaseModel):
    role_id: int
    skill_id: int
    importance: str

    model_config = ConfigDict(from_attributes=True)