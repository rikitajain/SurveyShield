from sqlalchemy.orm import Session

from app.database.crud import (
    get_respondent_by_device,
    count_device_usage
)

from app.database.rule_crud import get_rule
from app.config.settings import DEVICE_DUPLICATE_SCORE
from app.engine.rule_helper import get_rule_result

def check_device(
    db: Session,
    project_id: str,
    device_id: str,
) -> dict:

    respondent = get_respondent_by_device(
        db, 
        project_id,
        device_id
    )
    usage = count_device_usage(
        db, 
        project_id,
        device_id,
    )
    
    if respondent:
    
        rule = get_rule(
            db,
            project_id,
            "Device",
        )

        rule_data = get_rule_result(
            rule,
            DEVICE_DUPLICATE_SCORE,
            "High",
            "Duplicate Device ID",
        )
        
        if not rule_data["enabled"]:
            return {
                "engine": "Device",
                "score": 0,
                "matched": False,
                "severity": "None",
                "reason": "",
                "usage_count": usage
            }
        
        return {
            "engine": "Device",
            "score": rule_data["score"],
            "matched": True,
            "severity": rule_data["severity"],
            "reason": rule_data["reason"],
            "usage_count": usage
        }

    return {
        "engine": "Device",
        "score": 0,
        "matched": False,
        "severity": "None",
        "reason": "",
        "usage_count": usage
    }