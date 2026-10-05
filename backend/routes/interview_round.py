from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.schemas.interview_round import (
    InterviewRoundCreate,
    InterviewRoundUpdate,
    InterviewRoundResponse
)
from backend.service import interview_round as interview_round_service


router = APIRouter(
    prefix="/interview-rounds",
    tags=["Interview Rounds"]
)


# Create interview round
@router.post("/", response_model=InterviewRoundResponse)
def create_interview_round(
    round_data: InterviewRoundCreate,
    db: Session = Depends(get_db)
):
    return interview_round_service.create_interview_round(
        db,
        round_data
    )


# Get all interview rounds
@router.get("/", response_model=list[InterviewRoundResponse])
def get_all_interview_rounds(
    db: Session = Depends(get_db)
):
    return interview_round_service.get_all_interview_rounds(db)


# Get rounds for a particular application
@router.get(
    "/application/{application_id}",
    response_model=list[InterviewRoundResponse]
)
def get_rounds_by_application(
    application_id: int,
    db: Session = Depends(get_db)
):
    return interview_round_service.get_rounds_by_application(
        db,
        application_id
    )


# Get one interview round
@router.get(
    "/{round_id}",
    response_model=InterviewRoundResponse
)
def get_interview_round(
    round_id: int,
    db: Session = Depends(get_db)
):
    interview_round = interview_round_service.get_interview_round(
        db,
        round_id
    )

    if not interview_round:
        raise HTTPException(
            status_code=404,
            detail="Interview round not found"
        )

    return interview_round


# Update interview round
@router.put(
    "/{round_id}",
    response_model=InterviewRoundResponse
)
def update_interview_round(
    round_id: int,
    round_data: InterviewRoundUpdate,
    db: Session = Depends(get_db)
):
    interview_round = interview_round_service.update_interview_round(
        db,
        round_id,
        round_data
    )

    if not interview_round:
        raise HTTPException(
            status_code=404,
            detail="Interview round not found"
        )

    return interview_round


# Delete interview round
@router.delete(
    "/{round_id}",
    response_model=InterviewRoundResponse
)
def delete_interview_round(
    round_id: int,
    db: Session = Depends(get_db)
):
    interview_round = interview_round_service.delete_interview_round(
        db,
        round_id
    )

    if not interview_round:
        raise HTTPException(
            status_code=404,
            detail="Interview round not found"
        )

    return interview_round