from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from backend.database.dependencies import get_db , require_admin
from backend.models.user import User
from backend.schemas.role_skill import (
    RoleSkillCreate,
    RoleSkillUpdate,
    RoleSkillResponse
)
from backend.service import role_skill as role_skill_service


router = APIRouter(
    prefix="/roles",
    tags=["Role Skills"]
)


@router.post(
    "/{role_id}/skills",
    response_model=RoleSkillResponse
)
def add_role_skill(
    role_id: int,
    skill_data: RoleSkillCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    try:
        result = role_skill_service.add_role_skill(
            db,
            role_id,
            skill_data
        )

        if result == "role_not_found":
            raise HTTPException(
                status_code=404,
                detail="Role not found"
            )

        if result == "skill_not_found":
            raise HTTPException(
                status_code=404,
                detail="Skill not found"
            )
        return result

    except HTTPException:
        raise

    except Exception as e:
        db.rollback()

        print("ROLE SKILL ERROR:", e)

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@router.get(
    "/{role_id}/skills",
    response_model=list[RoleSkillResponse]
)
def get_role_skills(
    role_id: int,
    db: Session = Depends(get_db)
):
    return role_skill_service.get_role_skills(
        db,
        role_id
    )


@router.put(
    "/{role_id}/skills/{skill_id}",
    response_model=RoleSkillResponse
)
def update_role_skill(
    role_id: int,
    skill_id: int,
    skill_data: RoleSkillUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    role_skill = role_skill_service.update_role_skill(
        db,
        role_id,
        skill_id,
        skill_data
    )

    if not role_skill:
        raise HTTPException(
            status_code=404,
            detail="Role skill not found"
        )

    return role_skill


@router.delete(
    "/{role_id}/skills/{skill_id}",
    response_model=RoleSkillResponse
)
def delete_role_skill(
    role_id: int,
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    role_skill = role_skill_service.delete_role_skill(
        db,
        role_id,
        skill_id
    )

    if not role_skill:
        raise HTTPException(
            status_code=404,
            detail="Role skill not found"
        )

    return role_skill