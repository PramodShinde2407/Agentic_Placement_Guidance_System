from sqlalchemy.orm import Session

from backend.models.role_skill import RoleSkill
from backend.schemas.role_skill import RoleSkillCreate, RoleSkillUpdate
from backend.models.role import Role
from backend.models.skill import Skill


def add_role_skill(
    db: Session,
    role_id: int,
    skill_data: RoleSkillCreate
):
    role = db.query(Role).filter(
        Role.id == role_id
    ).first()

    if not role:
        return "role_not_found"

    skill = db.query(Skill).filter(
        Skill.id == skill_data.skill_id
    ).first()

    if not skill:
        return "skill_not_found"

    role_skill = RoleSkill(
        role_id=role_id,
        skill_id=skill_data.skill_id,
        importance=skill_data.importance
    )

    db.add(role_skill)
    db.commit()
    db.refresh(role_skill)

    return role_skill


def get_role_skills(
    db: Session,
    role_id: int
):
    return db.query(RoleSkill).filter(
        RoleSkill.role_id == role_id
    ).all()


def get_role_skill(
    db: Session,
    role_id: int,
    skill_id: int
):
    return db.query(RoleSkill).filter(
        RoleSkill.role_id == role_id,
        RoleSkill.skill_id == skill_id
    ).first()


def update_role_skill(
    db: Session,
    role_id: int,
    skill_id: int,
    skill_data: RoleSkillUpdate
):
    role_skill = get_role_skill(
        db,
        role_id,
        skill_id
    )

    if not role_skill:
        return None

    update_data = skill_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(role_skill, field, value)

    db.commit()
    db.refresh(role_skill)

    return role_skill


def delete_role_skill(
    db: Session,
    role_id: int,
    skill_id: int
):
    role_skill = get_role_skill(
        db,
        role_id,
        skill_id
    )

    if not role_skill:
        return None

    db.delete(role_skill)
    db.commit()

    return role_skill