from sqlalchemy.orm import Session

from backend.models.interview_experience import InterviewExperience
from backend.schemas.interview_experience import (
    InterviewExperienceCreate,
    InterviewExperienceUpdate
)


def create_interview_experience(
    db: Session,
    experience_data: InterviewExperienceCreate
):
    experience = InterviewExperience(
        **experience_data.model_dump(exclude_none=True)
    )

    db.add(experience)
    db.commit()
    db.refresh(experience)

    return experience


def get_all_interview_experiences(db: Session):
    return db.query(InterviewExperience).all()


def get_interview_experience(
    db: Session,
    experience_id: int
):
    return db.query(InterviewExperience).filter(
        InterviewExperience.id == experience_id
    ).first()


def get_experiences_by_company(
    db: Session,
    company_id: int
):
    return db.query(InterviewExperience).filter(
        InterviewExperience.company_id == company_id
    ).all()


def get_experiences_by_role(
    db: Session,
    role_id: int
):
    return db.query(InterviewExperience).filter(
        InterviewExperience.role_id == role_id
    ).all()


def update_interview_experience(
    db: Session,
    experience_id: int,
    experience_data: InterviewExperienceUpdate
):
    experience = get_interview_experience(db, experience_id)

    if not experience:
        return None

    update_data = experience_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(experience, field, value)

    db.commit()
    db.refresh(experience)

    return experience


def delete_interview_experience(
    db: Session,
    experience_id: int
):
    experience = get_interview_experience(db, experience_id)

    if not experience:
        return None

    db.delete(experience)
    db.commit()

    return experience