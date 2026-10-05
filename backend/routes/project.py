from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.schemas.project import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse
)
from backend.service import project as project_service


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("/", response_model=ProjectResponse)
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(get_db)
):
    return project_service.create_project(
        db,
        project_data
    )


@router.get("/", response_model=list[ProjectResponse])
def get_all_projects(
    db: Session = Depends(get_db)
):
    return project_service.get_all_projects(db)


@router.get("/student/{student_id}", response_model=list[ProjectResponse])
def get_projects_by_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    return project_service.get_projects_by_student(
        db,
        student_id
    )


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = project_service.get_project(
        db,
        project_id
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project


@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(
    project_id: int,
    project_data: ProjectUpdate,
    db: Session = Depends(get_db)
):
    project = project_service.update_project(
        db,
        project_id,
        project_data
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project


@router.delete("/{project_id}", response_model=ProjectResponse)
def delete_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = project_service.delete_project(
        db,
        project_id
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project