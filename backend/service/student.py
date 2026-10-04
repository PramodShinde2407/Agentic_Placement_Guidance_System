from sqlalchemy.orm import Session

from backend.models.student import Student
from backend.models.student_skill import StudentSkill
from backend.models.role_skill import RoleSkill
from backend.schemas.student import StudentCreate, StudentUpdate


def create_student(db: Session, student_data: StudentCreate):
    student = Student(
        **student_data.model_dump()
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


def get_all_students(db: Session):
    return db.query(Student).all()


def get_student(db: Session, student_id: int):
    return (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )


def update_student(
    db: Session,
    student_id: int,
    student_data: StudentUpdate
):
    student = get_student(db, student_id)

    if not student:
        return None

    update_data = student_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(student, field, value)

    db.commit()
    db.refresh(student)

    return student


def delete_student(db: Session, student_id: int):
    student = get_student(db, student_id)

    if not student:
        return None

    db.delete(student)
    db.commit()

    return student


def get_student_by_user_id(db: Session, user_id: int):

    return db.query(Student).filter(
        Student.user_id == user_id
    ).first()
    

def get_skill_gap(db: Session, student_id: int):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return None

    if not student.preferred_role_id:
        return {
            "student_id": student.id,
            "preferred_role": None,
            "required_skills": [],
            "student_skills": [],
            "missing_skills": []
        }

    role_skills = db.query(RoleSkill).filter(
        RoleSkill.role_id == student.preferred_role_id
    ).all()

    student_skills = db.query(StudentSkill).filter(
        StudentSkill.student_id == student.id
    ).all()

    required_skill_ids = {
        item.skill_id
        for item in role_skills
    }

    student_skill_ids = {
        item.skill_id
        for item in student_skills
    }

    missing_skill_ids = (
        required_skill_ids - student_skill_ids
    )

    return {
        "student_id": student.id,
        "preferred_role_id": student.preferred_role_id,
        "required_skill_ids": list(required_skill_ids),
        "student_skill_ids": list(student_skill_ids),
        "missing_skill_ids": list(missing_skill_ids)
    }