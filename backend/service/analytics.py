from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.models.placement import Placement
from backend.models.company import Company
from backend.models.role import Role
from backend.models.student import Student


# ==================================================
# 1. OVERALL PLACEMENT ANALYTICS
# ==================================================

def get_placement_overview(db: Session):

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


# ==================================================
# 2. COMPANY-WISE ANALYTICS
# ==================================================

def get_company_analytics(db: Session):

    results = db.query(
        Company.id.label("company_id"),
        Company.name.label("company_name"),
        func.count(Placement.id).label("total_placements"),
        func.avg(Placement.package_lpa).label("average_package"),
        func.max(Placement.package_lpa).label("highest_package")
    ).join(
        Placement,
        Placement.company_id == Company.id
    ).group_by(
        Company.id,
        Company.name
    ).order_by(
        func.count(Placement.id).desc()
    ).all()

    return [
        {
            "company_id": row.company_id,
            "company_name": row.company_name,
            "total_placements": row.total_placements,
            "average_package": row.average_package,
            "highest_package": row.highest_package
        }
        for row in results
    ]


# ==================================================
# 3. YEAR-WISE ANALYTICS
# ==================================================

def get_year_analytics(db: Session):

    results = db.query(
        Placement.placement_year.label("year"),
        func.count(Placement.id).label("total_placements"),
        func.avg(Placement.package_lpa).label("average_package"),
        func.max(Placement.package_lpa).label("highest_package")
    ).group_by(
        Placement.placement_year
    ).order_by(
        Placement.placement_year
    ).all()

    return [
        {
            "year": row.year,
            "total_placements": row.total_placements,
            "average_package": row.average_package,
            "highest_package": row.highest_package
        }
        for row in results
    ]


# ==================================================
# 4. ROLE-WISE ANALYTICS
# ==================================================

def get_role_analytics(db: Session):

    results = db.query(
        Role.id.label("role_id"),
        Role.name.label("role_name"),
        func.count(Placement.id).label("total_placements"),
        func.avg(Placement.package_lpa).label("average_package"),
        func.max(Placement.package_lpa).label("highest_package")
    ).join(
        Placement,
        Placement.role_id == Role.id
    ).group_by(
        Role.id,
        Role.name
    ).order_by(
        func.count(Placement.id).desc()
    ).all()

    return [
        {
            "role_id": row.role_id,
            "role_name": row.role_name,
            "total_placements": row.total_placements,
            "average_package": row.average_package,
            "highest_package": row.highest_package
        }
        for row in results
    ]


# ==================================================
# 5. BRANCH-WISE ANALYTICS
# ==================================================

def get_branch_analytics(db: Session):

    results = db.query(
        Student.branch.label("branch"),
        func.count(Placement.id).label("total_placements"),
        func.avg(Placement.package_lpa).label("average_package"),
        func.max(Placement.package_lpa).label("highest_package")
    ).join(
        Placement,
        Placement.student_id == Student.id
    ).group_by(
        Student.branch
    ).order_by(
        func.count(Placement.id).desc()
    ).all()

    return [
        {
            "branch": row.branch,
            "total_placements": row.total_placements,
            "average_package": row.average_package,
            "highest_package": row.highest_package
        }
        for row in results
    ]