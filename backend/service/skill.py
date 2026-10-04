from sqlalchemy.orm import Session

from backend.models.skill import Skill
from backend.schemas.skill import SkillCreate, SkillUpdate


def create_skill(db: Session, skill_data: SkillCreate):
    skill = Skill(
        **skill_data.model_dump()
    )

    db.add(skill)
    db.commit()
    db.refresh(skill)

    return skill


def get_all_skills(db: Session):
    return db.query(Skill).all()


def get_skill(db: Session, skill_id: int):
    return (
        db.query(Skill)
        .filter(Skill.id == skill_id)
        .first()
    )


def update_skill(
    db: Session,
    skill_id: int,
    skill_data: SkillUpdate
):
    skill = get_skill(db, skill_id)

    if not skill:
        return None

    update_data = skill_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(skill, field, value)

    db.commit()
    db.refresh(skill)

    return skill


def delete_skill(db: Session, skill_id: int):
    skill = get_skill(db, skill_id)

    if not skill:
        return None

    db.delete(skill)
    db.commit()

    return skill