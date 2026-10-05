from sqlalchemy.orm import Session

from backend.models.application import Application
from backend.schemas.application import ApplicationCreate, ApplicationUpdate


def create_application(db: Session, application_data: ApplicationCreate):
    application = Application(
        **application_data.model_dump(exclude_none=True)
    )

    db.add(application)
    db.commit()
    db.refresh(application)

    return application


def get_all_applications(db: Session):
    return db.query(Application).all()


def get_application(db: Session, application_id: int):
    return db.query(Application).filter(
        Application.id == application_id
    ).first()


def get_applications_by_student(db: Session, student_id: int):
    return db.query(Application).filter(
        Application.student_id == student_id
    ).all()


def get_applications_by_company(db: Session, company_id: int):
    return db.query(Application).filter(
        Application.company_id == company_id
    ).all()


def update_application(
    db: Session,
    application_id: int,
    application_data: ApplicationUpdate
):
    application = get_application(db, application_id)

    if not application:
        return None

    update_data = application_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(application, field, value)

    db.commit()
    db.refresh(application)

    return application


def delete_application(db: Session, application_id: int):
    application = get_application(db, application_id)

    if not application:
        return None

    db.delete(application)
    db.commit()

    return application