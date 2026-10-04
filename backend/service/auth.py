import hashlib
import bcrypt

from sqlalchemy.orm import Session

from backend.models.user import User
from backend.schemas.auth import RegisterRequest
from backend.utils.security import create_access_token


def prepare_password(password: str):
    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest().encode("utf-8")


def hash_password(password: str):
    password_bytes = prepare_password(password)

    return bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    ).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str):

    password_bytes = prepare_password(plain_password)

    return bcrypt.checkpw(
        password_bytes,
        hashed_password.encode("utf-8")
    )


def register_user(db: Session, user_data: RegisterRequest):

    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        return None

    hashed_password = hash_password(
        user_data.password
    )

    user = User(
        email=user_data.email,
        password_hash=hashed_password,
        role="student"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def login_user(db: Session, email: str, password: str):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return None

    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    token = create_access_token(
        user_id=user.id,
        role=user.role
    )

    return token