from pydantic import BaseModel
from typing import Optional


class EligibilityRuleCreate(BaseModel):
    company_id: int

    min_10th_marks: Optional[float] = None
    min_12th_marks: Optional[float] = None
    min_cgpa: Optional[float] = None

    allowed_branches: Optional[str] = None

    max_backlogs: Optional[int] = None
    active_backlog: bool = False
    passive_backlog: bool = False

    graduation_year: Optional[int] = None

    amcat_required: bool = False
    min_amcat_score: Optional[float] = None


class EligibilityRuleUpdate(BaseModel):
    min_10th_marks: Optional[float] = None
    min_12th_marks: Optional[float] = None
    min_cgpa: Optional[float] = None

    allowed_branches: Optional[str] = None

    max_backlogs: Optional[int] = None
    active_backlog: Optional[bool] = None
    passive_backlog: Optional[bool] = None

    graduation_year: Optional[int] = None

    amcat_required: Optional[bool] = None
    min_amcat_score: Optional[float] = None


class EligibilityRuleResponse(BaseModel):
    id: int
    company_id: int

    min_10th_marks: Optional[float]
    min_12th_marks: Optional[float]
    min_cgpa: Optional[float]

    allowed_branches: Optional[str]

    max_backlogs: Optional[int]
    active_backlog: bool
    passive_backlog: bool

    graduation_year: Optional[int]

    amcat_required: bool
    min_amcat_score: Optional[float]

    class Config:
        from_attributes = True