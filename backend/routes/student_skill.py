from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.schemas.student_skill import (
    StudentSkillCreate,
    StudentSkillUpdate,
    StudentSkillResponse
)
from backend.service import student_skill as student_skill_service


router = APIRouter(
    prefix="/students",
    tags=["Student Skills"]
)


@router.post(
    "/{student_id}/skills",
    response_model=StudentSkillResponse,
    status_code=status.HTTP_201_CREATED
)
def add_skill_to_student(
    student_id: int,
    skill_data: StudentSkillCreate,
    db: Session = Depends(get_db)
):
    try:
        return student_skill_service.add_student_skill(
            db,
            student_id,
            skill_data
        )

    except Exception as error:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


@router.get(
    "/{student_id}/skills",
    response_model=list[StudentSkillResponse]
)
def get_student_skills(
    student_id: int,
    db: Session = Depends(get_db)
):
    return student_skill_service.get_student_skills(
        db,
        student_id
    )


@router.put(
    "/{student_id}/skills/{skill_id}",
    response_model=StudentSkillResponse
)
def update_student_skill(
    student_id: int,
    skill_id: int,
    skill_data: StudentSkillUpdate,
    db: Session = Depends(get_db)
):
    student_skill = student_skill_service.update_student_skill(
        db,
        student_id,
        skill_id,
        skill_data
    )

    if not student_skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student skill not found"
        )

    return student_skill


@router.delete(
    "/{student_id}/skills/{skill_id}"
)
def delete_student_skill(
    student_id: int,
    skill_id: int,
    db: Session = Depends(get_db)
):
    student_skill = student_skill_service.delete_student_skill(
        db,
        student_id,
        skill_id
    )

    if not student_skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student skill not found"
        )

    return {
        "message": "Skill removed from student successfully",
        "student_id": student_id,
        "skill_id": skill_id
    }