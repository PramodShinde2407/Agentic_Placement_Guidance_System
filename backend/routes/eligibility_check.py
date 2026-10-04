from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db, get_current_user
from backend.models.user import User
from backend.schemas.eligibility_check import EligibilityCheckResponse
from backend.service import eligibility_check as eligibility_check_service
from backend.service import student as student_service


router = APIRouter(
    prefix="/eligibility",
    tags=["Eligibility Check"]
)


@router.get(
    "/check/{company_id}",
    response_model=EligibilityCheckResponse
)
def check_eligibility(
    company_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Get logged-in student's profile
    student = student_service.get_student_by_user_id(
        db,
        current_user.id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student profile not found"
        )

    result = eligibility_check_service.check_student_eligibility(
        db,
        student.id,
        company_id
    )

    if result == "company_not_found":
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    if result == "eligibility_rule_not_found":
        raise HTTPException(
            status_code=404,
            detail="Eligibility rules not found for this company"
        )

    if result == "student_not_found":
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return result