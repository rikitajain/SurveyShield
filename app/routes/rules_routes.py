from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.rule import Rule
from app.database.rule_crud import (
    create_rule,
    get_rules,
)

router = APIRouter(
    tags=["Rules"]
)

# ======================================
# Rules APIs
# ======================================   
@router.post(
    "/api/rules",
    summary="Create Rule"
)
def add_rule(
    rule: Rule,
    db: Session = Depends(get_db)
):

    return create_rule(
        db,
        rule.project_id,
        rule.engine,
        rule.enabled,
        rule.score,
        rule.severity,
        rule.action,
        rule.reason,
        rule.description,
    )

@router.get(
    "/api/rules/{project_id}",
    summary="Get Project Rules"
)
def list_rules(
    project_id: str,
    db: Session = Depends(get_db)
):

    return get_rules(
        db,
        project_id,
    )