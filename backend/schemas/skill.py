from pydantic import BaseModel, ConfigDict


class SkillCreate(BaseModel):
    name: str
    category: str | None = None


class SkillUpdate(BaseModel):
    name: str | None = None
    category: str | None = None


class SkillResponse(BaseModel):
    id: int
    name: str
    category: str | None = None

    model_config = ConfigDict(from_attributes=True)