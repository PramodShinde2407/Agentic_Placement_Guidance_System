from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.schemas.application import (
    ApplicationCreate,
    ApplicationUpdate,
    ApplicationResponse
)
from backend.service import application as application_service


router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)


# Create application
@router.post("/", response_model=ApplicationResponse)
def create_application(
    application_data: ApplicationCreate,
    db: Session = Depends(get_db)
):
    return application_service.create_application(
        db,
        application_data
    )


# Get all applications
@router.get("/", response_model=list[ApplicationResponse])
def get_all_applications(
    db: Session = Depends(get_db)
):
    return application_service.get_all_applications(db)


# Get applications of a student
@router.get(
    "/student/{student_id}",
    response_model=list[ApplicationResponse]
)
def get_applications_by_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    return application_service.get_applications_by_student(
        db,
        student_id
    )


# Get applications for a company
@router.get(
    "/company/{company_id}",
    response_model=list[ApplicationResponse]
)
def get_applications_by_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    return application_service.get_applications_by_company(
        db,
        company_id
    )


# Get one application
@router.get(
    "/{application_id}",
    response_model=ApplicationResponse
)
def get_application(
    application_id: int,
    db: Session = Depends(get_db)
):
    application = application_service.get_application(
        db,
        application_id
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application


# Update application
@router.put(
    "/{application_id}",
    response_model=ApplicationResponse
)
def update_application(
    application_id: int,
    application_data: ApplicationUpdate,
    db: Session = Depends(get_db)
):
    application = application_service.update_application(
        db,
        application_id,
        application_data
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application


# Delete application
@router.delete(
    "/{application_id}",
    response_model=ApplicationResponse
)
def delete_application(
    application_id: int,
    db: Session = Depends(get_db)
):
    application = application_service.delete_application(
        db,
        application_id
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application