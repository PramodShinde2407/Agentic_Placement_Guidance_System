from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.schemas.interview_experience import (
    InterviewExperienceCreate,
    InterviewExperienceUpdate,
    InterviewExperienceResponse
)
from backend.service import interview_experience as interview_experience_service


router = APIRouter(
    prefix="/interview-experiences",
    tags=["Interview Experiences"]
)


@router.post("/", response_model=InterviewExperienceResponse)
def create_interview_experience(
    experience_data: InterviewExperienceCreate,
    db: Session = Depends(get_db)
):
    return interview_experience_service.create_interview_experience(
        db,
        experience_data
    )


@router.get("/", response_model=list[InterviewExperienceResponse])
def get_all_interview_experiences(
    db: Session = Depends(get_db)
):
    return interview_experience_service.get_all_interview_experiences(db)


@router.get("/company/{company_id}", response_model=list[InterviewExperienceResponse])
def get_experiences_by_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    return interview_experience_service.get_experiences_by_company(
        db,
        company_id
    )


@router.get("/role/{role_id}", response_model=list[InterviewExperienceResponse])
def get_experiences_by_role(
    role_id: int,
    db: Session = Depends(get_db)
):
    return interview_experience_service.get_experiences_by_role(
        db,
        role_id
    )


@router.get("/{experience_id}", response_model=InterviewExperienceResponse)
def get_interview_experience(
    experience_id: int,
    db: Session = Depends(get_db)
):
    experience = interview_experience_service.get_interview_experience(
        db,
        experience_id
    )

    if not experience:
        raise HTTPException(
            status_code=404,
            detail="Interview experience not found"
        )

    return experience


@router.put("/{experience_id}", response_model=InterviewExperienceResponse)
def update_interview_experience(
    experience_id: int,
    experience_data: InterviewExperienceUpdate,
    db: Session = Depends(get_db)
):
    experience = interview_experience_service.update_interview_experience(
        db,
        experience_id,
        experience_data
    )

    if not experience:
        raise HTTPException(
            status_code=404,
            detail="Interview experience not found"
        )

    return experience


@router.delete("/{experience_id}", response_model=InterviewExperienceResponse)
def delete_interview_experience(
    experience_id: int,
    db: Session = Depends(get_db)
):
    experience = interview_experience_service.delete_interview_experience(
        db,
        experience_id
    )

    if not experience:
        raise HTTPException(
            status_code=404,
            detail="Interview experience not found"
        )

    return experience