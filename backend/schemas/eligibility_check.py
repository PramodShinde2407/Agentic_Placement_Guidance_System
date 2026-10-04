from pydantic import BaseModel


class EligibilityCheckResponse(BaseModel):
    eligible: bool
    company_id: int
    reasons: list[str]