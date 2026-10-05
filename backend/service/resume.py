from datetime import datetime

from sqlalchemy.orm import Session

from backend.models.resume import Resume
from backend.schemas.resume import ResumeCreate, ResumeUpdate


def create_resume(db: Session, resume_data: ResumeCreate):
    # If this resume is marked as current,
    # make all other resumes of this student non-current.
    if resume_data.is_current:
        db.query(Resume).filter(
            Resume.student_id == resume_data.student_id
        ).update(
            {"is_current": False},
            synchronize_session=False
        )

    resume = Resume(
        **resume_data.model_dump(exclude_none=True)
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return resume


def get_all_resumes(db: Session):
    return db.query(Resume).all()


def get_resume(db: Session, resume_id: int):
    return db.query(Resume).filter(
        Resume.id == resume_id
    ).first()


def get_resumes_by_student(db: Session, student_id: int):
    return db.query(Resume).filter(
        Resume.student_id == student_id
    ).all()


def get_current_resume(db: Session, student_id: int):
    return db.query(Resume).filter(
        Resume.student_id == student_id,
        Resume.is_current == True
    ).first()


def update_resume(
    db: Session,
    resume_id: int,
    resume_data: ResumeUpdate
):
    resume = get_resume(db, resume_id)

    if not resume:
        return None

    update_data = resume_data.model_dump(exclude_unset=True)

    # If this resume is being made current,
    # make other resumes of the same student non-current.
    if update_data.get("is_current") is True:
        db.query(Resume).filter(
            Resume.student_id == resume.student_id,
            Resume.id != resume.id
        ).update(
            {"is_current": False},
            synchronize_session=False
        )

    for field, value in update_data.items():
        setattr(resume, field, value)

    resume.updated_at = datetime.now()

    db.commit()
    db.refresh(resume)

    return resume


def delete_resume(db: Session, resume_id: int):
    resume = get_resume(db, resume_id)

    if not resume:
        return None

    db.delete(resume)
    db.commit()

    return resume