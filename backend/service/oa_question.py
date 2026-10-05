from sqlalchemy.orm import Session

from backend.models.oa_question import OAQuestion
from backend.schemas.oa_question import OAQuestionCreate, OAQuestionUpdate


def create_oa_question(db: Session, question_data: OAQuestionCreate):
    oa_question = OAQuestion(
        **question_data.model_dump(exclude_none=True)
    )

    db.add(oa_question)
    db.commit()
    db.refresh(oa_question)

    return oa_question


def get_all_oa_questions(db: Session):
    return db.query(OAQuestion).all()


def get_oa_question(db: Session, question_id: int):
    return db.query(OAQuestion).filter(
        OAQuestion.id == question_id
    ).first()


def get_oa_questions_by_company(db: Session, company_id: int):
    return db.query(OAQuestion).filter(
        OAQuestion.company_id == company_id
    ).all()


def update_oa_question(
    db: Session,
    question_id: int,
    question_data: OAQuestionUpdate
):
    oa_question = get_oa_question(db, question_id)

    if not oa_question:
        return None

    update_data = question_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(oa_question, field, value)

    db.commit()
    db.refresh(oa_question)

    return oa_question


def delete_oa_question(db: Session, question_id: int):
    oa_question = get_oa_question(db, question_id)

    if not oa_question:
        return None

    db.delete(oa_question)
    db.commit()

    return oa_question