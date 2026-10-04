from sqlalchemy.orm import Session

from backend.models.role import Role
from backend.schemas.role import RoleCreate, RoleUpdate


def create_role(db: Session, role_data: RoleCreate):
    role = Role(
        **role_data.model_dump()
    )

    db.add(role)
    db.commit()
    db.refresh(role)

    return role


def get_all_roles(db: Session):
    return db.query(Role).all()


def get_role(db: Session, role_id: int):
    return (
        db.query(Role)
        .filter(Role.id == role_id)
        .first()
    )


def update_role(
    db: Session,
    role_id: int,
    role_data: RoleUpdate
):
    role = get_role(db, role_id)

    if not role:
        return None

    update_data = role_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(role, field, value)

    db.commit()
    db.refresh(role)

    return role


def delete_role(db: Session, role_id: int):
    role = get_role(db, role_id)

    if not role:
        return None

    db.delete(role)
    db.commit()

    return role