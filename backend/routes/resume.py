from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.schemas.resume import (
    ResumeCreate,
    ResumeUpdate,
    ResumeResponse
)
from backend.service import resume as resume_service


router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"]
)


@router.post("/", response_model=ResumeResponse)
def create_resume(
    resume_data: ResumeCreate,
    db: Session = Depends(get_db)
):
    return resume_service.create_resume(
        db,
        resume_data
    )


@router.get("/", response_model=list[ResumeResponse])
def get_all_resumes(
    db: Session = Depends(get_db)
):
    return resume_service.get_all_resumes(db)


@router.get("/student/{student_id}", response_model=list[ResumeResponse])
def get_resumes_by_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    return resume_service.get_resumes_by_student(
        db,
        student_id
    )


@router.get("/student/{student_id}/current", response_model=ResumeResponse)
def get_current_resume(
    student_id: int,
    db: Session = Depends(get_db)
):
    resume = resume_service.get_current_resume(
        db,
        student_id
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Current resume not found"
        )

    return resume


@router.get("/{resume_id}", response_model=ResumeResponse)
def get_resume(
    resume_id: int,
    db: Session = Depends(get_db)
):
    resume = resume_service.get_resume(
        db,
        resume_id
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    return resume


@router.put("/{resume_id}", response_model=ResumeResponse)
def update_resume(
    resume_id: int,
    resume_data: ResumeUpdate,
    db: Session = Depends(get_db)
):
    resume = resume_service.update_resume(
        db,
        resume_id,
        resume_data
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    return resume


@router.delete("/{resume_id}", response_model=ResumeResponse)
def delete_resume(
    resume_id: int,
    db: Session = Depends(get_db)
):
    resume = resume_service.delete_resume(
        db,
        resume_id
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    return resume