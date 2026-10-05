from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db, require_admin
from backend.models.user import User
from backend.schemas.eligibility_rule import (
    EligibilityRuleCreate,
    EligibilityRuleUpdate,
    EligibilityRuleResponse
)

from backend.service import eligibility_rule as eligibility_rule_service


router = APIRouter(
    prefix="/eligibility-rules",
    tags=["Eligibility Rules"]
)


# CREATE
@router.post("/", response_model=EligibilityRuleResponse)
def create_eligibility_rule(
    rule_data: EligibilityRuleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    result = eligibility_rule_service.create_eligibility_rule(
        db,
        rule_data
    )

    if result == "company_not_found":
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    return result


# GET ALL
@router.get("/", response_model=list[EligibilityRuleResponse])
def get_all_eligibility_rules(
    db: Session = Depends(get_db)
):
    return eligibility_rule_service.get_all_eligibility_rules(db)


# GET BY COMPANY
@router.get(
    "/company/{company_id}",
    response_model=EligibilityRuleResponse
)
def get_eligibility_rule_by_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    rule = eligibility_rule_service.get_eligibility_rule_by_company(
        db,
        company_id
    )

    if not rule:
        raise HTTPException(
            status_code=404,
            detail="Eligibility rule not found for this company"
        )

    return rule


# GET BY ID
@router.get(
    "/{rule_id}",
    response_model=EligibilityRuleResponse
)
def get_eligibility_rule(
    rule_id: int,
    db: Session = Depends(get_db)
):
    rule = eligibility_rule_service.get_eligibility_rule(
        db,
        rule_id
    )

    if not rule:
        raise HTTPException(
            status_code=404,
            detail="Eligibility rule not found"
        )

    return rule


# UPDATE
@router.put(
    "/{rule_id}",
    response_model=EligibilityRuleResponse
)
def update_eligibility_rule(
    rule_id: int,
    rule_data: EligibilityRuleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    rule = eligibility_rule_service.update_eligibility_rule(
        db,
        rule_id,
        rule_data
    )

    if not rule:
        raise HTTPException(
            status_code=404,
            detail="Eligibility rule not found"
        )

    return rule


# DELETE
@router.delete(
    "/{rule_id}",
    response_model=EligibilityRuleResponse
)
def delete_eligibility_rule(
    rule_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    rule = eligibility_rule_service.delete_eligibility_rule(
        db,
        rule_id
    )

    if not rule:
        raise HTTPException(
            status_code=404,
            detail="Eligibility rule not found"
        )

    return rule