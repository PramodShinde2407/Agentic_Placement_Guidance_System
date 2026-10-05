from sqlalchemy.orm import Session

from backend.models.chat_history import ChatHistory
from backend.schemas.chat_history import ChatHistoryCreate


def create_chat_history(
    db: Session,
    chat_data: ChatHistoryCreate
):
    chat = ChatHistory(**chat_data.model_dump())

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return chat


def get_all_chat_history(db: Session):
    return db.query(ChatHistory).all()


def get_chat_history(db: Session, chat_id: int):
    return db.query(ChatHistory).filter(
        ChatHistory.id == chat_id
    ).first()


def get_chat_history_by_student(
    db: Session,
    student_id: int
):
    return db.query(ChatHistory).filter(
        ChatHistory.student_id == student_id
    ).order_by(ChatHistory.created_at).all()


def get_chat_history_by_session(
    db: Session,
    session_id: str
):
    return db.query(ChatHistory).filter(
        ChatHistory.session_id == session_id
    ).order_by(ChatHistory.created_at).all()


def delete_chat_history(
    db: Session,
    chat_id: int
):
    chat = get_chat_history(db, chat_id)

    if not chat:
        return None

    db.delete(chat)
    db.commit()

    return chat