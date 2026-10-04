from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.models.placement import Placement
from backend.schemas.placement import (
    PlacementCreate,
    PlacementUpdate
)


def create_placement(
    db: Session,
    placement_data: PlacementCreate
):
    placement = Placement(
        **placement_data.model_dump()
    )

    db.add(placement)
    db.commit()
    db.refresh(placement)

    return placement


def get_all_placements(db: Session):
    return db.query(Placement).all()


def get_placement(
    db: Session,
    placement_id: int
):
    return (
        db.query(Placement)
        .filter(Placement.id == placement_id)
        .first()
    )


def update_placement(
    db: Session,
    placement_id: int,
    placement_data: PlacementUpdate
):
    placement = get_placement(
        db,
        placement_id
    )

    if not placement:
        return None

    update_data = placement_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(placement, field, value)

    db.commit()
    db.refresh(placement)

    return placement


def delete_placement(
    db: Session,
    placement_id: int
):
    placement = get_placement(
        db,
        placement_id
    )

    if not placement:
        return None

    db.delete(placement)
    db.commit()

    return placement


def get_placements_by_company(
    db: Session,
    company_id: int
):
    return (
        db.query(Placement)
        .filter(Placement.company_id == company_id)
        .all()
    )


def get_placements_by_student(
    db: Session,
    student_id: int
):
    return (
        db.query(Placement)
        .filter(Placement.student_id == student_id)
        .all()
    )
    
def get_placement_statistics(db: Session):
    result = db.query(
        func.count(Placement.id).label("total_placements"),
        func.avg(Placement.package_lpa).label("average_package"),
        func.max(Placement.package_lpa).label("highest_package"),
        func.min(Placement.package_lpa).label("lowest_package")
    ).first()

    return {
        "total_placements": result.total_placements,
        "average_package": result.average_package,
        "highest_package": result.highest_package,
        "lowest_package": result.lowest_package
    }