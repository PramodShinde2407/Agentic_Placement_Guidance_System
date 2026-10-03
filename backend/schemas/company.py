from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CompanyCreate(BaseModel):
    name: str
    industry: str | None = None
    website: str | None = None
    location: str | None = None
    description: str | None = None


class CompanyUpdate(BaseModel):
    name: str | None = None
    industry: str | None = None
    website: str | None = None
    location: str | None = None
    description: str | None = None


class CompanyResponse(BaseModel):
    id: int
    name: str
    industry: str | None = None
    website: str | None = None
    location: str | None = None
    description: str | None = None
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)