from sqlalchemy.orm import Session
from app.database.audit_models import AuditLog

def get_all_audit_logs(db: Session):

    return (
        db.query(AuditLog)
        .order_by(AuditLog.created_at.desc())
        .all()
    )
    
def create_audit_log(
    db: Session,
    project_id,
    email,
    ip,
    device_id,
    risk_score,
    decision,
    engine_results,
):

    log = AuditLog(
        project_id=project_id,
        email=email,
        ip=ip,
        device_id=device_id,
        risk_score=risk_score,
        decision=decision,
        matched_engines=engine_results,
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log