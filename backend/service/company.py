from sqlalchemy.orm import Session

from backend.models.company import Company
from backend.schemas.company import CompanyCreate, CompanyUpdate


def create_company(
    db: Session,
    company_data: CompanyCreate
):
    company = Company(
        **company_data.model_dump()
    )

    db.add(company)
    db.commit()
    db.refresh(company)

    return company


def get_all_companies(db: Session):
    return db.query(Company).all()


def get_company(
    db: Session,
    company_id: int
):
    return (
        db.query(Company)
        .filter(Company.id == company_id)
        .first()
    )


def update_company(
    db: Session,
    company_id: int,
    company_data: CompanyUpdate
):
    company = get_company(
        db,
        company_id
    )

    if not company:
        return None

    update_data = company_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(company, field, value)

    db.commit()
    db.refresh(company)

    return company


def delete_company(
    db: Session,
    company_id: int
):
    company = get_company(
        db,
        company_id
    )

    if not company:
        return None

    db.delete(company)
    db.commit()

    return company