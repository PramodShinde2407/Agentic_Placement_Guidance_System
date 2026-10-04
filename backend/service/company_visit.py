from sqlalchemy.orm import Session

from backend.models.company_visit import CompanyVisit
from backend.schemas.company_visit import (
    CompanyVisitCreate,
    CompanyVisitUpdate
)


def create_company_visit(
    db: Session,
    visit_data: CompanyVisitCreate
):
    company_visit = CompanyVisit(
        **visit_data.model_dump()
    )

    db.add(company_visit)
    db.commit()
    db.refresh(company_visit)

    return company_visit


def get_all_company_visits(db: Session):
    return db.query(CompanyVisit).all()


def get_company_visit(
    db: Session,
    visit_id: int
):
    return db.query(CompanyVisit).filter(
        CompanyVisit.id == visit_id
    ).first()


def get_company_visits_by_company(
    db: Session,
    company_id: int
):
    return db.query(CompanyVisit).filter(
        CompanyVisit.company_id == company_id
    ).all()


def update_company_visit(
    db: Session,
    visit_id: int,
    visit_data: CompanyVisitUpdate
):
    company_visit = get_company_visit(
        db,
        visit_id
    )

    if not company_visit:
        return None

    update_data = visit_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(company_visit, field, value)

    db.commit()
    db.refresh(company_visit)

    return company_visit


def delete_company_visit(
    db: Session,
    visit_id: int
):
    company_visit = get_company_visit(
        db,
        visit_id
    )

    if not company_visit:
        return None

    db.delete(company_visit)
    db.commit()

    return company_visit