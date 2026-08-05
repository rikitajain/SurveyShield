from sqlalchemy.orm import Session

from app.database.crud import get_respondent_by_email
from app.database.rule_crud import get_rule
from app.config.settings import EMAIL_DUPLICATE_SCORE
from app.engine.rule_helper import get_rule_result

def check_email(
    db: Session,
    project_id: str,
    email: str,
) -> dict:

    respondent = get_respondent_by_email(
        db,
        project_id,
        email,
    )

    if respondent:

        rule = get_rule(
            db,
            project_id,
            "Email",
        )
        
        rule_data = get_rule_result(
            rule,
            EMAIL_DUPLICATE_SCORE,
            "High",
            "Duplicate Email",
        )

        if not rule_data["enabled"]:
            return {
                "engine": "Email",
                "score": 0,
                "matched": False,
                "severity": "None",
                "reason": "",
            }
                
        return {
            "engine": "Email",
            "score": rule_data["score"],
            "matched": True,
            "severity": rule_data["severity"],
            "reason": rule_data["reason"],
        }

    return {
        "engine": "Email",
        "score": 0,
        "matched": False,
        "severity": "None",
        "reason": "",
    }