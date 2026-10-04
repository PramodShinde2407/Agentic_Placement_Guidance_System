from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.schemas.skill import (
    SkillCreate,
    SkillUpdate,
    SkillResponse
)
from backend.service import skill as skill_service


router = APIRouter(
    prefix="/skills",
    tags=["Skills"]
)


@router.post(
    "/",
    response_model=SkillResponse,
    status_code=status.HTTP_201_CREATED
)
def create_skill(
    skill_data: SkillCreate,
    db: Session = Depends(get_db)
):
    return skill_service.create_skill(
        db,
        skill_data
    )


@router.get(
    "/",
    response_model=list[SkillResponse]
)
def get_skills(
    db: Session = Depends(get_db)
):
    return skill_service.get_all_skills(db)


@router.get(
    "/{skill_id}",
    response_model=SkillResponse
)
def get_skill(
    skill_id: int,
    db: Session = Depends(get_db)
):
    skill = skill_service.get_skill(
        db,
        skill_id
    )

    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found"
        )

    return skill


@router.put(
    "/{skill_id}",
    response_model=SkillResponse
)
def update_skill(
    skill_id: int,
    skill_data: SkillUpdate,
    db: Session = Depends(get_db)
):
    skill = skill_service.update_skill(
        db,
        skill_id,
        skill_data
    )

    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found"
        )

    return skill


@router.delete("/{skill_id}")
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db)
):
    skill = skill_service.delete_skill(
        db,
        skill_id
    )

    if not skill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Skill not found"
        )

    return {
        "message": "Skill deleted successfully",
        "skill_id": skill_id
    }