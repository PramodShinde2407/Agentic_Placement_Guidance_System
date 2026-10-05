from pydantic import BaseModel
from typing import Optional


# --------------------------------------------------
# 1. Overall Placement Analytics
# --------------------------------------------------

class PlacementOverviewResponse(BaseModel):
    total_placements: int
    average_package: Optional[float]
    highest_package: Optional[float]
    lowest_package: Optional[float]


# --------------------------------------------------
# 2. Company-wise Analytics
# --------------------------------------------------

class CompanyAnalyticsResponse(BaseModel):
    company_id: int
    company_name: str
    total_placements: int
    average_package: Optional[float]
    highest_package: Optional[float]


# --------------------------------------------------
# 3. Year-wise Analytics
# --------------------------------------------------

class YearAnalyticsResponse(BaseModel):
    year: int
    total_placements: int
    average_package: Optional[float]
    highest_package: Optional[float]


# --------------------------------------------------
# 4. Role-wise Analytics
# --------------------------------------------------

class RoleAnalyticsResponse(BaseModel):
    role_id: int
    role_name: str
    total_placements: int
    average_package: Optional[float]
    highest_package: Optional[float]
    

# --------------------------------------------------
# 5. Branch-wise Analytics
# --------------------------------------------------

class BranchAnalyticsResponse(BaseModel):
    branch: str
    total_placements: int
    average_package: Optional[float]
    highest_package: Optional[float]