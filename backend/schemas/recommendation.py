from pydantic import BaseModel
from typing import Optional


class CompanyRecommendationResponse(BaseModel):
    company_id: int
    company_name: str

    match_percentage: float

    required_skills: list[str]
    student_skills: list[str]
    matched_skills: list[str]
    missing_skills: list[str]

    average_package: Optional[float] = None
    highest_package: Optional[float] = None
    
class RoleRecommendationResponse(BaseModel):
    role_id: int
    role_name: str

    match_percentage: float

    required_skills: list[str]
    student_skills: list[str]
    matched_skills: list[str]
    missing_skills: list[str]