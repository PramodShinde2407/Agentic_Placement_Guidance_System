from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db, get_current_user
from backend.models.user import User


from backend.schemas.recommendation import (
    CompanyRecommendationResponse,
    RoleRecommendationResponse
)

from backend.service import recommendation as recommendation_service
from backend.service import student as student_service


router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.get(
    "/companies",
    response_model=list[CompanyRecommendationResponse]
)
def get_company_recommendations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # --------------------------------------------------
    # Get logged-in student's profile
    # --------------------------------------------------

    student = student_service.get_student_by_user_id(
        db,
        current_user.id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student profile not found"
        )

    # --------------------------------------------------
    # Get recommendations
    # --------------------------------------------------

    result = recommendation_service.get_company_recommendations(
        db,
        student.id
    )

    if result == "student_not_found":
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    if result == "preferred_role_not_found":
        raise HTTPException(
            status_code=400,
            detail="Please set your preferred role first"
        )

    return result

@router.get(
    "/roles",
    response_model=list[RoleRecommendationResponse]
)
def get_role_recommendations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # --------------------------------------------------
    # Get logged-in student's profile
    # --------------------------------------------------

    student = student_service.get_student_by_user_id(
        db,
        current_user.id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student profile not found"
        )

    # --------------------------------------------------
    # Get role recommendations
    # --------------------------------------------------

    result = recommendation_service.get_role_recommendations(
        db,
        student.id
    )

    if result == "student_not_found":
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return result