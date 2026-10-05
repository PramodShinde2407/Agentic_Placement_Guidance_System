from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.schemas.chat_history import (
    ChatHistoryCreate,
    ChatHistoryResponse
)
from backend.service import chat_history as chat_history_service


router = APIRouter(
    prefix="/chat-history",
    tags=["Chat History"]
)


@router.post("/", response_model=ChatHistoryResponse)
def create_chat_history(
    chat_data: ChatHistoryCreate,
    db: Session = Depends(get_db)
):
    return chat_history_service.create_chat_history(
        db,
        chat_data
    )


@router.get("/", response_model=list[ChatHistoryResponse])
def get_all_chat_history(
    db: Session = Depends(get_db)
):
    return chat_history_service.get_all_chat_history(db)


@router.get(
    "/student/{student_id}",
    response_model=list[ChatHistoryResponse]
)
def get_chat_history_by_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    return chat_history_service.get_chat_history_by_student(
        db,
        student_id
    )


@router.get(
    "/session/{session_id}",
    response_model=list[ChatHistoryResponse]
)
def get_chat_history_by_session(
    session_id: str,
    db: Session = Depends(get_db)
):
    return chat_history_service.get_chat_history_by_session(
        db,
        session_id
    )


@router.get(
    "/{chat_id}",
    response_model=ChatHistoryResponse
)
def get_chat_history(
    chat_id: int,
    db: Session = Depends(get_db)
):
    chat = chat_history_service.get_chat_history(
        db,
        chat_id
    )

    if not chat:
        raise HTTPException(
            status_code=404,
            detail="Chat history not found"
        )

    return chat


@router.delete(
    "/{chat_id}",
    response_model=ChatHistoryResponse
)
def delete_chat_history(
    chat_id: int,
    db: Session = Depends(get_db)
):
    chat = chat_history_service.delete_chat_history(
        db,
        chat_id
    )

    if not chat:
        raise HTTPException(
            status_code=404,
            detail="Chat history not found"
        )

    return chat