from sqlalchemy.orm import Session

from backend.models.interview_round import InterviewRound
from backend.schemas.interview_round import (
    InterviewRoundCreate,
    InterviewRoundUpdate
)


def create_interview_round(
    db: Session,
    round_data: InterviewRoundCreate
):
    interview_round = InterviewRound(
        **round_data.model_dump(exclude_none=True)
    )

    db.add(interview_round)
    db.commit()
    db.refresh(interview_round)

    return interview_round


def get_all_interview_rounds(db: Session):
    return db.query(InterviewRound).all()


def get_interview_round(
    db: Session,
    round_id: int
):
    return db.query(InterviewRound).filter(
        InterviewRound.id == round_id
    ).first()


def get_rounds_by_application(
    db: Session,
    application_id: int
):
    return db.query(InterviewRound).filter(
        InterviewRound.application_id == application_id
    ).order_by(
        InterviewRound.round_number
    ).all()


def update_interview_round(
    db: Session,
    round_id: int,
    round_data: InterviewRoundUpdate
):
    interview_round = get_interview_round(db, round_id)

    if not interview_round:
        return None

    update_data = round_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(interview_round, field, value)

    db.commit()
    db.refresh(interview_round)

    return interview_round


def delete_interview_round(
    db: Session,
    round_id: int
):
    interview_round = get_interview_round(db, round_id)

    if not interview_round:
        return None

    db.delete(interview_round)
    db.commit()

    return interview_round