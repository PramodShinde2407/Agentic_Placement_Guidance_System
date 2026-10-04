from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db

from backend.schemas.placement import (
    PlacementCreate,
    PlacementUpdate,
    PlacementResponse
)

from backend.service import placement as placement_service


router = APIRouter(
    prefix="/placements",
    tags=["Placements"]
)


# =========================================================
# CREATE / GET ALL PLACEMENTS
# =========================================================

@router.post(
    "/",
    response_model=PlacementResponse,
    status_code=status.HTTP_201_CREATED
)
def create_placement(
    placement_data: PlacementCreate,
    db: Session = Depends(get_db)
):
    return placement_service.create_placement(
        db,
        placement_data
    )


@router.get(
    "/",
    response_model=list[PlacementResponse]
)
def get_placements(
    db: Session = Depends(get_db)
):
    return placement_service.get_all_placements(db)


# =========================================================
# SPECIFIC / FILTERED ROUTES
# =========================================================

@router.get(
    "/company/{company_id}",
    response_model=list[PlacementResponse]
)
def get_company_placements(
    company_id: int,
    db: Session = Depends(get_db)
):
    return placement_service.get_placements_by_company(
        db,
        company_id
    )


@router.get(
    "/student/{student_id}",
    response_model=list[PlacementResponse]
)
def get_student_placements(
    student_id: int,
    db: Session = Depends(get_db)
):
    return placement_service.get_placements_by_student(
        db,
        student_id
    )


@router.get(
    "/statistics"
)
def get_placement_statistics(
    db: Session = Depends(get_db)
):
    return placement_service.get_placement_statistics(db)


# =========================================================
# SINGLE PLACEMENT BY ID
# Keep dynamic {placement_id} routes at the END
# =========================================================

@router.get(
    "/{placement_id}",
    response_model=PlacementResponse
)
def get_placement(
    placement_id: int,
    db: Session = Depends(get_db)
):
    placement = placement_service.get_placement(
        db,
        placement_id
    )

    if not placement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Placement not found"
        )

    return placement


@router.put(
    "/{placement_id}",
    response_model=PlacementResponse
)
def update_placement(
    placement_id: int,
    placement_data: PlacementUpdate,
    db: Session = Depends(get_db)
):
    placement = placement_service.update_placement(
        db,
        placement_id,
        placement_data
    )

    if not placement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Placement not found"
        )

    return placement


@router.delete(
    "/{placement_id}"
)
def delete_placement(
    placement_id: int,
    db: Session = Depends(get_db)
):
    placement = placement_service.delete_placement(
        db,
        placement_id
    )

    if not placement:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Placement not found"
        )

    return {
        "message": "Placement deleted successfully",
        "placement_id": placement_id
    }