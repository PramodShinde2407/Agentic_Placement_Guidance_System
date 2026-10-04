from sqlalchemy.orm import Session

from backend.models.eligibility_rule import EligibilityRule
from backend.models.company import Company

from backend.schemas.eligibility_rule import (
    EligibilityRuleCreate,
    EligibilityRuleUpdate
)


def create_eligibility_rule(
    db: Session,
    rule_data: EligibilityRuleCreate
):
    # Check whether company exists
    company = db.query(Company).filter(
        Company.id == rule_data.company_id
    ).first()

    if not company:
        return "company_not_found"

    rule = EligibilityRule(
        **rule_data.model_dump()
    )

    db.add(rule)
    db.commit()
    db.refresh(rule)

    return rule


def get_all_eligibility_rules(db: Session):
    return db.query(EligibilityRule).all()


def get_eligibility_rule(
    db: Session,
    rule_id: int
):
    return db.query(EligibilityRule).filter(
        EligibilityRule.id == rule_id
    ).first()


def get_eligibility_rule_by_company(
    db: Session,
    company_id: int
):
    return db.query(EligibilityRule).filter(
        EligibilityRule.company_id == company_id
    ).first()


def update_eligibility_rule(
    db: Session,
    rule_id: int,
    rule_data: EligibilityRuleUpdate
):
    rule = get_eligibility_rule(db, rule_id)

    if not rule:
        return None

    update_data = rule_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(rule, field, value)

    db.commit()
    db.refresh(rule)

    return rule


def delete_eligibility_rule(
    db: Session,
    rule_id: int
):
    rule = get_eligibility_rule(db, rule_id)

    if not rule:
        return None

    db.delete(rule)
    db.commit()

    return rule