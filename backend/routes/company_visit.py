from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db, require_admin
from backend.schemas.company_visit import (
    CompanyVisitCreate,
    CompanyVisitUpdate,
    CompanyVisitResponse
)
from backend.service import company_visit as company_visit_service
from backend.models.user import User

router = APIRouter(
    prefix="/company-visits",
    tags=["Company Visits"]
)


@router.post(
    "/",
    response_model=CompanyVisitResponse
)
def create_company_visit(
    visit_data: CompanyVisitCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return company_visit_service.create_company_visit(
        db,
        visit_data
    )


@router.get(
    "/",
    response_model=list[CompanyVisitResponse]
)
def get_all_company_visits(
    db: Session = Depends(get_db)
):
    return company_visit_service.get_all_company_visits(db)


@router.get(
    "/company/{company_id}",
    response_model=list[CompanyVisitResponse]
)
def get_company_visits_by_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    return company_visit_service.get_company_visits_by_company(
        db,
        company_id
    )


@router.get(
    "/{visit_id}",
    response_model=CompanyVisitResponse
)
def get_company_visit(
    visit_id: int,
    db: Session = Depends(get_db)
):
    company_visit = company_visit_service.get_company_visit(
        db,
        visit_id
    )

    if not company_visit:
        raise HTTPException(
            status_code=404,
            detail="Company visit not found"
        )

    return company_visit


@router.put(
    "/{visit_id}",
    response_model=CompanyVisitResponse
)
def update_company_visit(
    visit_id: int,
    visit_data: CompanyVisitUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    company_visit = company_visit_service.update_company_visit(
        db,
        visit_id,
        visit_data
    )

    if not company_visit:
        raise HTTPException(
            status_code=404,
            detail="Company visit not found"
        )

    return company_visit


@router.delete(
    "/{visit_id}",
    response_model=CompanyVisitResponse
)
def delete_company_visit(
    visit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    company_visit = company_visit_service.delete_company_visit(
        db,
        visit_id
    )

    if not company_visit:
        raise HTTPException(
            status_code=404,
            detail="Company visit not found"
        )

    return company_visit