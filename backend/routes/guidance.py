from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db, get_current_user
from backend.models.user import User
from backend.schemas.guidance import SkillGapResponse
from backend.service import student as student_service


router = APIRouter(
    prefix="/guidance",
    tags=["Guidance"]
)


@router.get(
    "/skill-gap",
    response_model=SkillGapResponse
)
def get_my_skill_gap(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    student = student_service.get_student_by_user_id(
        db,
        current_user.id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student profile not found"
        )

    result = student_service.get_skill_gap(
        db,
        student.id
    )

    return result