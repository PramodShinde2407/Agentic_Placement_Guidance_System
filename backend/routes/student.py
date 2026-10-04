from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.database.dependencies import (
    get_db,
    get_current_user
)
from backend.schemas.student import (
    StudentCreate,
    StudentUpdate,
    StudentResponse
)
from backend.models.user import User
from backend.service import student as student_service
from backend.schemas.auth import UserResponse

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student_data: StudentCreate,
    db: Session = Depends(get_db)
):
    return student_service.create_student(
        db,
        student_data
    )


@router.get(
    "/",
    response_model=list[StudentResponse]
)
def get_students(
    db: Session = Depends(get_db)
):
    return student_service.get_all_students(db)


@router.get("/my-user", response_model=UserResponse)
def get_my_user(
    current_user: User = Depends(get_current_user)
):
    return current_user


@router.get(
    "/my-profile",
    response_model=StudentResponse
)
def get_my_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    student = student_service.get_student_by_user_id(
        db,
        current_user.id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student profile not found"
        )

    return student


@router.get(
    "/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = student_service.get_student(
        db,
        student_id
    )

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student


@router.put(
    "/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db)
):
    student = student_service.update_student(
        db,
        student_id,
        student_data
    )

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student


@router.delete(
    "/{student_id}"
)
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = student_service.delete_student(
        db,
        student_id
    )

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully",
        "student_id": student_id
    }
    

