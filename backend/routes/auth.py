from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import (
    get_db,
    get_current_user,
    require_admin,
    require_student
)
from backend.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
    UserResponse
)
from backend.models.user import User
from backend.service.auth import (
    register_user,
    login_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user_data: RegisterRequest,
    db: Session = Depends(get_db)
):

    user = register_user(db, user_data)

    if user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return user

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    user_data: LoginRequest,
    db: Session = Depends(get_db)
):

    token = login_user(
        db,
        user_data.email,
        user_data.password
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
    
    
@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user = Depends(get_current_user)
):

    return current_user

@router.get("/admin-test")
def admin_test(
    current_user: User = Depends(require_admin)
):
    return {
        "message": "You have admin access",
        "user_id": current_user.id,
        "role": current_user.role
    }


@router.get("/student-test")
def student_test(
    current_user: User = Depends(require_student)
):
    return {
        "message": "You have student access",
        "user_id": current_user.id,
        "role": current_user.role
    }