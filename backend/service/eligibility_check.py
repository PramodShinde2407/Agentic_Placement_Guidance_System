from sqlalchemy.orm import Session

from backend.models.student import Student
from backend.models.company import Company
from backend.models.eligibility_rule import EligibilityRule


def check_student_eligibility(
    db: Session,
    student_id: int,
    company_id: int
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return "student_not_found"

    company = db.query(Company).filter(
        Company.id == company_id
    ).first()

    if not company:
        return "company_not_found"

    rule = db.query(EligibilityRule).filter(
        EligibilityRule.company_id == company_id
    ).first()

    if not rule:
        return "eligibility_rule_not_found"

    reasons = []
    eligible = True

    # 10th marks
    if rule.min_10th_marks is not None:
        if (
            student.marks_10th is None
            or student.marks_10th < rule.min_10th_marks
        ):
            eligible = False
            reasons.append(
                f"10th marks requirement not satisfied: "
                f"minimum {rule.min_10th_marks}% required"
            )
        else:
            reasons.append("10th marks requirement satisfied")

    # 12th marks
    if rule.min_12th_marks is not None:
        if (
            student.marks_12th is None
            or student.marks_12th < rule.min_12th_marks
        ):
            eligible = False
            reasons.append(
                f"12th marks requirement not satisfied: "
                f"minimum {rule.min_12th_marks}% required"
            )
        else:
            reasons.append("12th marks requirement satisfied")

    # CGPA
    if rule.min_cgpa is not None:
        if (
            student.cgpa is None
            or student.cgpa < rule.min_cgpa
        ):
            eligible = False
            reasons.append(
                f"CGPA requirement not satisfied: "
                f"minimum {rule.min_cgpa} required"
            )
        else:
            reasons.append("CGPA requirement satisfied")

    # Branch
    if rule.allowed_branches:
        allowed_branches = [
            branch.strip().lower()
            for branch in rule.allowed_branches.split(",")
        ]

        if (
            student.branch is None
            or student.branch.lower() not in allowed_branches
        ):
            eligible = False
            reasons.append(
                f"Branch requirement not satisfied: "
                f"allowed branches are {rule.allowed_branches}"
            )
        else:
            reasons.append("Branch requirement satisfied")

    # Active backlog
    if rule.active_backlog is False:
        if student.active_backlog is True:
            eligible = False
            reasons.append(
                "Active backlog is not allowed"
            )
        else:
            reasons.append(
                "Active backlog requirement satisfied"
            )

    # Passive backlog
    if rule.passive_backlog is False:
        if student.passive_backlog is True:
            eligible = False
            reasons.append(
                "Passive backlog is not allowed"
            )
        else:
            reasons.append(
                "Passive backlog requirement satisfied"
            )

    # Graduation year
    if rule.graduation_year is not None:
        if (
            student.graduation_year is None
            or student.graduation_year != rule.graduation_year
        ):
            eligible = False
            reasons.append(
                f"Graduation year requirement not satisfied: "
                f"required {rule.graduation_year}"
            )
        else:
            reasons.append(
                "Graduation year requirement satisfied"
            )

    # AMCAT
    if rule.amcat_required:
        if student.amcat_score is None:
            eligible = False
            reasons.append(
                "AMCAT score is required"
            )
        elif (
            rule.min_amcat_score is not None
            and student.amcat_score < rule.min_amcat_score
        ):
            eligible = False
            reasons.append(
                f"AMCAT score requirement not satisfied: "
                f"minimum {rule.min_amcat_score} required"
            )
        else:
            reasons.append(
                "AMCAT requirement satisfied"
            )

    # Maximum total backlogs
    if rule.max_backlogs is not None:
        total_backlogs = (
            int(student.active_backlog)
            + int(student.passive_backlog)
        )

        if total_backlogs > rule.max_backlogs:
            eligible = False
            reasons.append(
                f"Maximum backlog requirement not satisfied: "
                f"maximum {rule.max_backlogs} allowed"
            )
        else:
            reasons.append(
                "Maximum backlog requirement satisfied"
            )

    return {
        "eligible": eligible,
        "company_id": company_id,
        "reasons": reasons
    }