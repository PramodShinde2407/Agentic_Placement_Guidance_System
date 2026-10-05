from sqlalchemy.orm import Session

from backend.models.project import Project
from backend.schemas.project import ProjectCreate, ProjectUpdate


def create_project(db: Session, project_data: ProjectCreate):
    project = Project(
        **project_data.model_dump(exclude_none=True)
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project


def get_all_projects(db: Session):
    return db.query(Project).all()


def get_project(db: Session, project_id: int):
    return db.query(Project).filter(
        Project.id == project_id
    ).first()


def get_projects_by_student(db: Session, student_id: int):
    return db.query(Project).filter(
        Project.student_id == student_id
    ).all()


def update_project(
    db: Session,
    project_id: int,
    project_data: ProjectUpdate
):
    project = get_project(db, project_id)

    if not project:
        return None

    update_data = project_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(project, field, value)

    db.commit()
    db.refresh(project)

    return project


def delete_project(db: Session, project_id: int):
    project = get_project(db, project_id)

    if not project:
        return None

    db.delete(project)
    db.commit()

    return project