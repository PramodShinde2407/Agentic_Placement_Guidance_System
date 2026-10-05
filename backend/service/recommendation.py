from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.models.student import Student
from backend.models.student_skill import StudentSkill
from backend.models.skill import Skill
from backend.models.role_skill import RoleSkill
from backend.models.company import Company
from backend.models.placement import Placement
from backend.models.role import Role

def get_company_recommendations(
    db: Session,
    student_id: int
):
    # --------------------------------------------------
    # 1. Get student
    # --------------------------------------------------

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return "student_not_found"

    # --------------------------------------------------
    # 2. Check preferred role
    # --------------------------------------------------

    if not student.preferred_role_id:
        return "preferred_role_not_found"

    # --------------------------------------------------
    # 3. Get skills of the student
    # --------------------------------------------------

    student_skill_rows = db.query(
        Skill.id,
        Skill.name
    ).join(
        StudentSkill,
        StudentSkill.skill_id == Skill.id
    ).filter(
        StudentSkill.student_id == student_id
    ).all()

    student_skill_ids = {
        row.id for row in student_skill_rows
    }

    student_skill_names = [
        row.name for row in student_skill_rows
    ]

    # --------------------------------------------------
    # 4. Get required skills for preferred role
    # --------------------------------------------------

    role_skill_rows = db.query(
        Skill.id,
        Skill.name
    ).join(
        RoleSkill,
        RoleSkill.skill_id == Skill.id
    ).filter(
        RoleSkill.role_id == student.preferred_role_id
    ).all()

    required_skill_ids = {
        row.id for row in role_skill_rows
    }

    required_skill_names = [
        row.name for row in role_skill_rows
    ]

    # --------------------------------------------------
    # 5. Calculate matched and missing skills
    # --------------------------------------------------

    matched_skill_ids = (
        student_skill_ids & required_skill_ids
    )

    missing_skill_ids = (
        required_skill_ids - student_skill_ids
    )

    matched_skills = [
        row.name
        for row in role_skill_rows
        if row.id in matched_skill_ids
    ]

    missing_skills = [
        row.name
        for row in role_skill_rows
        if row.id in missing_skill_ids
    ]

    # --------------------------------------------------
    # 6. Calculate match percentage
    # --------------------------------------------------

    if len(required_skill_ids) == 0:
        match_percentage = 0.0
    else:
        match_percentage = (
            len(matched_skill_ids)
            / len(required_skill_ids)
        ) * 100

    # --------------------------------------------------
    # 7. Get companies
    # --------------------------------------------------

    companies = db.query(Company).all()

    recommendations = []

    # --------------------------------------------------
    # 8. Calculate company recommendation
    # --------------------------------------------------

    for company in companies:

        # Get placement statistics for this company

        placement_stats = db.query(
            func.avg(Placement.package_lpa).label(
                "average_package"
            ),
            func.max(Placement.package_lpa).label(
                "highest_package"
            )
        ).filter(
            Placement.company_id == company.id
        ).first()

        recommendations.append({
            "company_id": company.id,
            "company_name": company.name,

            "match_percentage": round(
                match_percentage,
                2
            ),

            "required_skills": required_skill_names,

            "student_skills": student_skill_names,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "average_package": (
                float(placement_stats.average_package)
                if placement_stats.average_package is not None
                else None
            ),

            "highest_package": (
                float(placement_stats.highest_package)
                if placement_stats.highest_package is not None
                else None
            )
        })

    # --------------------------------------------------
    # 9. Sort by match percentage
    # --------------------------------------------------

    recommendations.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    return recommendations



def get_role_recommendations(
    db: Session,
    student_id: int
):
    # --------------------------------------------------
    # 1. Check student
    # --------------------------------------------------

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return "student_not_found"

    # --------------------------------------------------
    # 2. Get student's skills
    # --------------------------------------------------

    student_skill_rows = db.query(
        Skill.id,
        Skill.name
    ).join(
        StudentSkill,
        StudentSkill.skill_id == Skill.id
    ).filter(
        StudentSkill.student_id == student_id
    ).all()

    student_skill_ids = {
        row.id for row in student_skill_rows
    }

    student_skill_names = [
        row.name for row in student_skill_rows
    ]

    # --------------------------------------------------
    # 3. Get all roles
    # --------------------------------------------------

    roles = db.query(Role).all()

    recommendations = []

    # --------------------------------------------------
    # 4. Check every role
    # --------------------------------------------------

    for role in roles:

        role_skill_rows = db.query(
            Skill.id,
            Skill.name
        ).join(
            RoleSkill,
            RoleSkill.skill_id == Skill.id
        ).filter(
            RoleSkill.role_id == role.id
        ).all()

        required_skill_ids = {
            row.id for row in role_skill_rows
        }

        required_skill_names = [
            row.name for row in role_skill_rows
        ]

        # --------------------------------------------------
        # If role has no skills
        # --------------------------------------------------

        if len(required_skill_ids) == 0:
            match_percentage = 0.0
            matched_skills = []
            missing_skills = required_skill_names

        else:

            # --------------------------------------------------
            # Find matched skills
            # --------------------------------------------------

            matched_skill_ids = (
                student_skill_ids & required_skill_ids
            )

            missing_skill_ids = (
                required_skill_ids - student_skill_ids
            )

            matched_skills = [
                row.name
                for row in role_skill_rows
                if row.id in matched_skill_ids
            ]

            missing_skills = [
                row.name
                for row in role_skill_rows
                if row.id in missing_skill_ids
            ]

            # --------------------------------------------------
            # Calculate percentage
            # --------------------------------------------------

            match_percentage = (
                len(matched_skill_ids)
                / len(required_skill_ids)
            ) * 100

        # --------------------------------------------------
        # Add recommendation
        # --------------------------------------------------

        recommendations.append({
            "role_id": role.id,
            "role_name": role.name,

            "match_percentage": round(
                match_percentage,
                2
            ),

            "required_skills": required_skill_names,

            "student_skills": student_skill_names,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills
        })

    # --------------------------------------------------
    # 5. Sort highest match first
    # --------------------------------------------------

    recommendations.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    return recommendations