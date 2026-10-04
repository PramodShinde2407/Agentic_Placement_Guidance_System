from sqlalchemy.orm import Session

from backend.models.student_skill import StudentSkill
from backend.schemas.student_skill import (
    StudentSkillCreate,
    StudentSkillUpdate
)


def add_student_skill(
    db: Session,
    student_id: int,
    skill_data: StudentSkillCreate
):
    student_skill = StudentSkill(
        student_id=student_id,
        skill_id=skill_data.skill_id,
        proficiency=skill_data.proficiency,
        years_experience=skill_data.years_experience
    )

    db.add(student_skill)
    db.commit()
    db.refresh(student_skill)

    return student_skill


def get_student_skills(
    db: Session,
    student_id: int
):
    return (
        db.query(StudentSkill)
        .filter(StudentSkill.student_id == student_id)
        .all()
    )


def get_student_skill(
    db: Session,
    student_id: int,
    skill_id: int
):
    return (
        db.query(StudentSkill)
        .filter(
            StudentSkill.student_id == student_id,
            StudentSkill.skill_id == skill_id
        )
        .first()
    )


def update_student_skill(
    db: Session,
    student_id: int,
    skill_id: int,
    skill_data: StudentSkillUpdate
):
    student_skill = get_student_skill(
        db,
        student_id,
        skill_id
    )

    if not student_skill:
        return None

    update_data = skill_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(student_skill, field, value)

    db.commit()
    db.refresh(student_skill)

    return student_skill


def delete_student_skill(
    db: Session,
    student_id: int,
    skill_id: int
):
    student_skill = get_student_skill(
        db,
        student_id,
        skill_id
    )

    if not student_skill:
        return None

    db.delete(student_skill)
    db.commit()

    return student_skill