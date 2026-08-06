from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
import json

from app.database.db import get_db
from app.models.respondent import Respondent

from app.engine.engines import run_all_engines
from app.engine.risk_engine import calculate_risk
from app.engine.decision_engine import get_decision
from app.engine.geo_engine import get_ip_location

from app.database.crud import create_respondent
from app.database.audit_crud import create_audit_log

from app.logger.logger import logger

router = APIRouter(
    tags=["Respondents"]
)

# ======================================
# Respondent APIs
# ======================================

@router.post(
    "/api/respondent/check",
    summary="Check respondent for fraud"
)

def check_respondent(
    request: Request,
    respondent: Respondent,
    db: Session = Depends(get_db)
):
    # 1. Get client IP
    client_ip = request.client.host
    # 2. Get Geo
    geo = get_ip_location(client_ip)
    
    logger.info(f"Client IP: {client_ip}")
    logger.info(f"Geo Location: {geo}")
    
    engine_results = run_all_engines(
        db,
        respondent,
        client_ip,
    )
    
    risk = calculate_risk(engine_results)
    
    # Step 5 - Decision
    decision = get_decision(risk["risk_score"])

    # Step 6 - Save only if accepted
    if decision == "ACCEPT":
        create_respondent(
            db,
            respondent.project_id,
            respondent.uuid,
            respondent.vendor,
            respondent.email,
            client_ip,
            respondent.country,
            respondent.browser,
            respondent.device_id,
            respondent.latitude,
            respondent.longitude,
            respondent.location_permission,
            respondent.location_accuracy,
        )

    engine_results_json = json.dumps(engine_results)
    
    # Step 7 - Audit Log
    
    create_audit_log(
        db,
        respondent.project_id,
        respondent.email,
        client_ip,
        respondent.device_id,
        risk["risk_score"],
        decision,
        engine_results_json,
    )
    
    return {
        "decision": decision,
        "risk_score": risk["risk_score"],
        "engines": engine_results,
        "reasons": risk["reasons"]
    }
    
    # 8. Return response