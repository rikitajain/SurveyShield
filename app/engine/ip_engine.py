from sqlalchemy.orm import Session

from app.database.crud import get_respondent_by_ip
from app.database.rule_crud import get_rule
from app.config.settings import IP_DUPLICATE_SCORE
from app.engine.rule_helper import get_rule_result

def check_ip(
    db: Session,
    project_id: str,
    ip: str,
) -> dict:

    respondent = get_respondent_by_ip(
        db, 
        project_id,
        ip
    )

    if respondent:
    
        rule = get_rule(
            db,
            project_id,
            "IP",
        )

        rule_data = get_rule_result(
            rule,
            IP_DUPLICATE_SCORE,
            "Medium",
            "Duplicate IP",
        )
        
        if not rule_data["enabled"]:
            return {
                "engine": "IP",
                "score": 0,
                "matched": False,
                "severity": "None",
                "reason": "",
            }
         
        return {
            "engine": "IP",
            "score": rule_data["score"],
            "matched": True,
            "severity": rule_data["severity"],
            "reason": rule_data["reason"],
        }

    return {
        "engine": "IP",
        "score": 0,
        "matched": False,
        "severity": "None",
        "reason": ""
    }