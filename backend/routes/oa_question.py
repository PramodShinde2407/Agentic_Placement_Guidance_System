from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db,require_admin
from backend.schemas.oa_question import (
    OAQuestionCreate,
    OAQuestionUpdate,
    OAQuestionResponse
)
from backend.service import oa_question as oa_question_service
from backend.models.user import User

router = APIRouter(
    prefix="/oa-questions",
    tags=["OA Questions"]
)


@router.post("/", response_model=OAQuestionResponse)
def create_oa_question(
    question_data: OAQuestionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    return oa_question_service.create_oa_question(
        db,
        question_data
    )


@router.get("/", response_model=list[OAQuestionResponse])
def get_all_oa_questions(
    db: Session = Depends(get_db)
):
    return oa_question_service.get_all_oa_questions(db)


@router.get("/company/{company_id}", response_model=list[OAQuestionResponse])
def get_oa_questions_by_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    return oa_question_service.get_oa_questions_by_company(
        db,
        company_id
    )


@router.get("/{question_id}", response_model=OAQuestionResponse)
def get_oa_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    question = oa_question_service.get_oa_question(
        db,
        question_id
    )

    if not question:
        raise HTTPException(
            status_code=404,
            detail="OA question not found"
        )

    return question


@router.put("/{question_id}", response_model=OAQuestionResponse)
def update_oa_question(
    question_id: int,
    question_data: OAQuestionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    question = oa_question_service.update_oa_question(
        db,
        question_id,
        question_data
    )

    if not question:
        raise HTTPException(
            status_code=404,
            detail="OA question not found"
        )

    return question


@router.delete("/{question_id}", response_model=OAQuestionResponse)
def delete_oa_question(
    question_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    question = oa_question_service.delete_oa_question(
        db,
        question_id
    )

    if not question:
        raise HTTPException(
            status_code=404,
            detail="OA question not found"
        )

    return question