from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db

from backend.schemas.analytics import (
    PlacementOverviewResponse,
    CompanyAnalyticsResponse,
    YearAnalyticsResponse,
    RoleAnalyticsResponse,
    BranchAnalyticsResponse
)

from backend.service import analytics as analytics_service


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


# ==================================================
# 1. OVERALL PLACEMENT ANALYTICS
# ==================================================

@router.get(
    "/overview",
    response_model=PlacementOverviewResponse
)
def get_placement_overview(
    db: Session = Depends(get_db)
):
    return analytics_service.get_placement_overview(db)


# ==================================================
# 2. COMPANY-WISE ANALYTICS
# ==================================================

@router.get(
    "/companies",
    response_model=list[CompanyAnalyticsResponse]
)
def get_company_analytics(
    db: Session = Depends(get_db)
):
    return analytics_service.get_company_analytics(db)


# ==================================================
# 3. YEAR-WISE ANALYTICS
# ==================================================

@router.get(
    "/years",
    response_model=list[YearAnalyticsResponse]
)
def get_year_analytics(
    db: Session = Depends(get_db)
):
    return analytics_service.get_year_analytics(db)


# ==================================================
# 4. ROLE-WISE ANALYTICS
# ==================================================

@router.get(
    "/roles",
    response_model=list[RoleAnalyticsResponse]
)
def get_role_analytics(
    db: Session = Depends(get_db)
):
    return analytics_service.get_role_analytics(db)

# ==================================================
# 5. BRANCH-WISE ANALYTICS
# ==================================================

@router.get(
    "/branches",
    response_model=list[BranchAnalyticsResponse]
)
def get_branch_analytics(
    db: Session = Depends(get_db)
):
    return analytics_service.get_branch_analytics(db)