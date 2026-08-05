from sqlalchemy.orm import Session
from app.database.rule_models import ProjectRule


def create_rule(
    db: Session,
    project_id,
    engine,
    enabled,
    score,
    severity,
    action,
    reason,
    description,
):

    rule = ProjectRule(
        project_id=project_id,
        engine=engine,
        enabled=enabled,
        score=score,
        severity=severity,
        action=action,
        reason=reason,
        description=description,
)

    db.add(rule)
    db.commit()
    db.refresh(rule)

    return rule


def get_rules(
    db: Session,
    project_id,
):

    return (
        db.query(ProjectRule)
        .filter(ProjectRule.project_id == project_id)
        .all()
    )


def get_rule(
    db: Session,
    project_id,
    engine,
):

    return (
        db.query(ProjectRule)
        .filter(
            ProjectRule.project_id == project_id,
            ProjectRule.engine == engine,
        )
        .first()
    )